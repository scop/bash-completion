import os
import sys
from itertools import chain

import pytest

from conftest import (
    assert_bash_exec,
    assert_complete,
    bash_env_saved,
    get_testdir,
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
                ["config", "known_hosts", "local_path/", r"spaced\ \ conf"],
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
                ["config", "known_hosts", "local_path/", r"spaced\ \ conf"],
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

    @pytest.mark.complete("scp -Fempty", cwd="shared")
    def test_capital_f_without_space_3(self, completion):
        assert completion == "_dir/"

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

    def test_remote_path_with_backslash(self, bash):
        assert_bash_exec(
            bash, r"ssh() { printf '%s\n' 'abc def.txt' 'abc\ def.txt'; }"
        )
        completion = assert_complete(bash, "scp remote_host:abc\\")
        assert_bash_exec(bash, "unset -f ssh")

        # Note: The number of backslash escaping differs depending on the scp
        # version.
        assert completion == sorted(
            [r"abc\ def.txt", r"abc\\\ def.txt"]
        ) or completion == sorted([r"abc\\\ def.txt", r"abc\\\\\\\ def.txt"])

    def test_xfunc_remote_files(self, live_pwd, bash):
        def prefix_paths(prefix, paths):
            return [f"{prefix}{path}" for path in paths]

        with bash_env_saved(bash) as bash_env:
            bash_env.save_variable("COMPREPLY")
            bash_env.write_variable(
                "cur", f"{LIVE_HOST}:{get_testdir()}/fixtures/shared/default/"
            )
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
        assert completions_regular_escape == prefix_paths(
            f"{get_testdir()}/fixtures/shared/default/",
            [
                "bar ",
                r"bar\\\ bar.d/",
                "foo ",
                "foo.d/",
            ],
        )
        assert completions_less_escape == prefix_paths(
            f"{get_testdir()}/fixtures/shared/default/",
            [
                "bar ",
                r"bar\ bar.d/",
                "foo ",
                "foo.d/",
            ],
        )

    @pytest.fixture
    def tmpdir_backslash(self, request, bash):
        if sys.platform.startswith("win"):
            pytest.skip("Filenames not allowed on Windows")

        tmpdir = prepare_fixture_dir(
            request, files=["local_path-file\\"], dirs=[]
        )
        return tmpdir

    def test_local_path_ending_with_backslash(self, bash, tmpdir_backslash):
        completion = assert_complete(
            bash, "scp local_path-", cwd=tmpdir_backslash
        )
        assert completion.output == r"file\\ "

    def test_remote_path_ending_with_backslash(self, bash):
        assert_bash_exec(bash, "ssh() { echo 'hypothetical\\'; }")
        completion = assert_complete(bash, "scp remote_host:hypo")
        assert_bash_exec(bash, "unset -f ssh")
        assert completion.output == r"thetical\\\\ "

    @pytest.fixture
    def tmpdir_mkfifo(self, request, bash):
        # We prepare two files: 1) a named pipe and 2) a regular file ending
        # with the same name but an extra special character "|".
        tmpdir = prepare_fixture_dir(
            request,
            files=["local_path_2-pipe|"],
            dirs=[],
        )

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

    # FIXME: This test currently fails.
    # def test_local_path_mark_2(self, bash, tmpdir_mkfifo):
    #     completion = assert_complete(
    #         bash, "scp local_path_2-", cwd=tmpdir_mkfifo
    #     )
    #     assert completion == "pipe\\|"

    @pytest.mark.complete("scp spa", cwd="scp")
    def test_local_path_with_spaces_1(self, completion):
        assert completion == r"ced\ \ conf"

    @pytest.mark.complete(r"scp spaced\ ", cwd="scp")
    def test_local_path_with_spaces_2(self, completion):
        assert completion == r"\ conf"

    @pytest.mark.complete("scp backslash-a\\", cwd="scp/local_path")
    def test_local_path_backslash(self, completion):
        assert completion == sorted(
            [r"backslash-a\ b.txt", r"backslash-a\\\ b.txt"]
        )
