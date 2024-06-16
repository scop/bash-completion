from itertools import chain

import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env="^[+-](COMPREPLY|BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE)=",
)
class TestUnitCompgenKnownHosts:
    @pytest.mark.parametrize(
        "prefix,colon_flag,hostfile",
        [("", "", True), ("", "", False), ("user@", "c", True)],
    )
    def test_basic(
        self, bash, hosts, avahi_hosts, prefix, colon_flag, hostfile
    ):
        expected = (
            "%s%s%s" % (prefix, x, ":" if colon_flag else "")
            for x in chain(
                hosts if hostfile else avahi_hosts,
                # fixtures/_known_hosts/config
                "gee hus jar #not-a-comment".split(),
                # fixtures/_known_hosts/known_hosts
                (
                    "doo",
                    "ike",
                    "jub",
                    "10.0.0.1",
                    "kyl",
                    "100.0.0.2",
                    "10.10.0.3",
                    "blah",
                    "fd00:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:5555",
                    "fe80::123:0xff:dead:beef%eth0",
                    "1111:2222:3333:4444:5555:6666:xxxx:abab",
                    "11xx:2222:3333:4444:5555:6666:xxxx:abab",
                    "::42",
                ),
            )
        )
        assert_bash_exec(
            bash,
            "unset -v BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE"
            if hostfile
            else "BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE=",
        )
        output = assert_bash_exec(
            bash,
            "_comp_compgen_known_hosts -a%sF _known_hosts/config '%s'; "
            r'printf "%%s\n" "${COMPREPLY[@]}"; unset -v COMPREPLY'
            % (colon_flag, prefix),
            want_output=True,
        )
        assert sorted(set(output.split())) == sorted(expected)

    @pytest.mark.parametrize(
        "family,result",
        (
            ("4", "127.0.0.1 localhost"),
            ("6", "::1 localhost"),
            ("46", "localhost"),
        ),
    )
    def test_ip_filtering(self, bash, family, result):
        assert_bash_exec(
            bash,
            "unset -v COMPREPLY BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE",
        )
        output = assert_bash_exec(
            bash,
            "BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE= "
            "_comp_compgen_known_hosts -%sF _known_hosts/localhost_config ''; "
            r'printf "%%s\n" "${COMPREPLY[@]}"' % family,
            want_output=True,
        )
        assert sorted(set(output.strip().split())) == sorted(result.split())

    def test_consecutive_spaces(self, bash, hosts):
        expected = hosts.copy()
        # fixtures/_known_hosts/spaced  conf
        expected.extend("gee hus #not-a-comment".split())
        # fixtures/_known_hosts/known_hosts2
        expected.extend("two two2 two3 two4".split())
        # fixtures/_known_hosts_/spaced  known_hosts
        expected.extend("doo ike".split())

        output = assert_bash_exec(
            bash,
            "unset -v COMPREPLY BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE; "
            "_comp_compgen_known_hosts -aF '_known_hosts/spaced  conf' ''; "
            r'printf "%s\n" "${COMPREPLY[@]}"',
            want_output=True,
        )
        assert sorted(set(output.strip().split())) == sorted(expected)

    def test_files_starting_with_tilde(self, bash, hosts):
        expected = hosts.copy()
        # fixtures/_known_hosts/known_hosts2
        expected.extend("two two2 two3 two4".split())
        # fixtures/_known_hosts/known_hosts3
        expected.append("three")
        # fixtures/_known_hosts/known_hosts4
        expected.append("four")

        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("HOME", bash.cwd)
            output = assert_bash_exec(
                bash,
                "unset -v COMPREPLY BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE;"
                " _comp_compgen_known_hosts -aF _known_hosts/config_tilde ''; "
                r'printf "%s\n" "${COMPREPLY[@]}"',
                want_output=True,
            )

        assert sorted(set(output.strip().split())) == sorted(expected)

    def test_included_configs(self, bash, hosts):
        expected = hosts.copy()
        # fixtures/_known_hosts/config_include_recursion
        expected.append("recursion")
        # fixtures/_known_hosts/.ssh/config_relative_path
        expected.append("relative_path")
        # fixtures/_known_hosts/.ssh/config_asterisk_*
        expected.extend("asterisk_1 asterisk_2".split())
        # fixtures/_known_hosts/.ssh/config_question_mark
        expected.append("question_mark")

        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("HOME", "%s/_known_hosts" % bash.cwd)
            output = assert_bash_exec(
                bash,
                "unset -v COMPREPLY BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE;"
                " _comp_compgen_known_hosts -aF _known_hosts/config_include ''; "
                r'printf "%s\n" "${COMPREPLY[@]}"',
                want_output=True,
            )
        assert sorted(set(output.strip().split())) == sorted(expected)

    def test_no_globbing(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("HOME", "%s/_known_hosts" % bash.cwd)
            bash_env.chdir("_known_hosts")
            output = assert_bash_exec(
                bash,
                "unset -v COMPREPLY BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE;"
                " _comp_compgen_known_hosts -aF config ''; "
                r'printf "%s\n" "${COMPREPLY[@]}"',
                want_output=True,
            )
        completion = sorted(set(output.strip().split()))
        assert "gee" in completion
        assert "gee-filename-canary" not in completion
