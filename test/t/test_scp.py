import os
from itertools import chain

import pytest

from conftest import (
    assert_bash_exec,
    assert_complete,
    bash_env_saved,
    prepare_fixture_dir,
)

LIVE_HOST = os.environ.get(
    "BASH_COMPLETION_TEST_LIVE_SSH_HOST", default="bash_completion"
)


class TestScp:
    @pytest.mark.complete("scp -F config ", cwd="scp")
    def test_basic(self, hosts, completion):
        expected = sorted(
            chain(
                (
                    "%s:" % x
                    for x in chain(
                        hosts,
                        # From fixtures/scp/config
                        "gee hut".split(),
                        # From fixtures/scp/known_hosts
                        "blah doo ike".split(),
                    )
                ),
                # Local filenames
                ["bin/", "config", "known_hosts", r"spaced\ \ conf"],
            )
        )
        assert completion == expected

    @pytest.mark.complete("scp -F 'spaced  conf' ", cwd="scp")
    def test_basic_spaced_conf(self, hosts, completion):
        expected = sorted(
            chain(
                (
                    "%s:" % x
                    for x in chain(
                        hosts,
                        # From "fixtures/scp/spaced  conf"
                        "gee jar".split(),
                        # From fixtures/scp/known_hosts
                        "blah doo ike".split(),
                    )
                ),
                # Local filenames
                ["bin/", "config", "known_hosts", r"spaced\ \ conf"],
            )
        )
        assert completion == expected

    @pytest.mark.complete("scp -F")
    def test_capital_f_without_space(self, completion):
        assert completion
        assert not any(
            "option requires an argument -- F" in x for x in completion
        )

    @pytest.mark.complete("scp -Fconf", cwd="scp")
    def test_capital_f_without_space_2(self, completion):
        assert completion == "ig"

    @pytest.mark.complete("scp -Fbi", cwd="scp")
    def test_capital_f_without_space_3(self, completion):
        assert completion == "n/"

    @pytest.fixture(scope="class")
    def live_pwd(self, bash):
        try:
            return assert_bash_exec(
                bash,
                "ssh -o 'Batchmode yes' -o 'ConnectTimeout 1' "
                "%s pwd 2>/dev/null" % LIVE_HOST,
                want_output=True,
            ).strip()
        except AssertionError:
            pytest.skip("Live host %s not available" % LIVE_HOST)

    @pytest.mark.complete("scp %s:" % LIVE_HOST, sleep_after_tab=2)
    def test_live(self, live_pwd, completion):
        """
        To support this test, configure a HostName entry for LIVE_HOST
        in ssh's configs, e.g. ~/.ssh/config or /etc/ssh/ssh_config.

        Connection to it must open sufficiently quickly for the
        ConnectTimeout and sleep_after_tab settings.
        """
        assert completion == f"{live_pwd}/"

    @pytest.mark.complete("scp -o Foo=")
    def test_option_arg(self, completion):
        assert not completion  # and no errors either

    @pytest.mark.complete(
        "scp hostname-not-expected-to-exist-in-known-hosts:",
        shopt=dict(nullglob=True),
    )
    def test_remote_path_with_nullglob(self, completion):
        assert not completion

    @pytest.mark.complete(
        "scp hostname-not-expected-to-exist-in-known-hosts:",
        shopt=dict(failglob=True),
    )
    def test_remote_path_with_failglob(self, completion):
        assert not completion

    def test_remote_path_with_spaces(self, bash):
        assert_bash_exec(bash, "ssh() { echo 'spaces in filename.txt'; }")
        completion = assert_complete(bash, "scp remote_host:spaces")
        assert_bash_exec(bash, "unset -f ssh")
        assert completion == r"\\\ in\\\ filename.txt"

    def test_xfunc_remote_files(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.save_variable("COMPREPLY")
            bash_env.write_variable(
                "PATH",
                "$PWD/scp/bin:$PATH",
                quote=False,
            )
            bash_env.write_variable("cur", "local:shared/default/")
            completions_regular_escape = (
                assert_bash_exec(
                    bash,
                    r'_comp_compgen -x scp remote_files; printf "%s\n" "${COMPREPLY[@]}"',
                    want_output=True,
                )
                .strip()
                .splitlines()
            )
            completions_less_escape = (
                assert_bash_exec(
                    bash,
                    r'_comp_compgen -x scp remote_files -l; printf "%s\n" "${COMPREPLY[@]}"',
                    want_output=True,
                )
                .strip()
                .splitlines()
            )
        assert completions_regular_escape == [
            "shared/default/bar ",
            r"shared/default/bar\\\ bar.d/",
            "shared/default/foo ",
            "shared/default/foo.d/",
        ]
        assert completions_less_escape == [
            "shared/default/bar ",
            r"shared/default/bar\ bar.d/",
            "shared/default/foo ",
            "shared/default/foo.d/",
        ]

    @pytest.fixture
    def tmpdir_mkfifo(self, request, bash):
        tmpdir, _, _ = prepare_fixture_dir(request, files=[], dirs=[])

        # If the system allows creating a named pipe, we create it in a
        # temporary directory and returns the path.  We cannot check the
        # availability of the named pipe simply by the existence of the command
        # "mkfifo" Even if the command "mkfifo" exists in the system, the
        # current operating system or the filesystem may not allow creating a
        # named pipe.
        try:
            assert_bash_exec(bash, "mkfifo '%s/local_path_1-pipe'" % tmpdir)
        except Exception:
            pytest.skip(
                "The present system does not allow creating a named pipe through 'mkfifo'."
            )

        return tmpdir

    def test_local_path_mark_1(self, bash, tmpdir_mkfifo):
        completion = assert_complete(
            bash, "scp local_path_1-", cwd=tmpdir_mkfifo
        )
        assert completion == "pipe"
