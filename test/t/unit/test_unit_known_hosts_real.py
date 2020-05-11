from itertools import chain

import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None, ignore_env="^[+-]COMP(REPLY|_KNOWN_HOSTS_WITH_HOSTFILE)="
)
class TestUnitKnownHostsReal:
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
                # fixtures/_known_hosts_real/config
                "gee hus jar".split(),
                # fixtures/_known_hosts_real/known_hosts
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
            "unset -v COMP_KNOWN_HOSTS_WITH_HOSTFILE"
            if hostfile
            else "COMP_KNOWN_HOSTS_WITH_HOSTFILE=",
        )
        output = assert_bash_exec(
            bash,
            "_known_hosts_real -a%sF _known_hosts_real/config '%s'; "
            r'printf "%%s\n" "${COMPREPLY[@]}"; unset COMPREPLY'
            % (colon_flag, prefix),
            want_output=True,
        )
        assert sorted(output.split()) == sorted(expected)

    @pytest.mark.parametrize(
        "family,result",
        (
            ("4", "127.0.0.1 localhost"),
            ("6", "::1 localhost"),
            ("46", "localhost"),
        ),
    )
    def test_ip_filtering(self, bash, family, result):
        assert_bash_exec(bash, "unset COMPREPLY")
        output = assert_bash_exec(
            bash,
            "COMP_KNOWN_HOSTS_WITH_HOSTFILE= "
            "_known_hosts_real -%sF _known_hosts_real/localhost_config ''; "
            r'printf "%%s\n" "${COMPREPLY[@]}"' % family,
            want_output=True,
        )
        assert sorted(output.strip().split()) == sorted(result.split())
