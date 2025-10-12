import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(ignore_env=r"^[+-]_comp_cmd_scp__path_esc=")
class TestRsync:
    @pytest.mark.complete("rsync ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rsync --rsh ")
    def test_2(self, completion):
        assert completion == "rsh ssh".split()

    @pytest.mark.complete("rsync --rsh=")
    def test_3(self, completion):
        assert completion == "rsh ssh".split()

    @pytest.mark.complete("rsync --", require_longopt=True)
    def test_4(self, completion):
        assert "--compress" in completion
        assert "--timeout=" in completion

    @pytest.mark.parametrize(
        "ver1,ver2,result",
        [
            ("1", "1", "="),
            ("1", "2", "<"),
            ("2", "1", ">"),
            ("1.1", "1.2", "<"),
            ("1.2", "1.1", ">"),
            ("1.1", "1.1.1", "<"),
            ("1.1.1", "1.1", ">"),
            ("1.1.1", "1.1.1", "="),
            ("2.1", "2.2", "<"),
            ("3.0.4.10", "3.0.4.2", ">"),
            ("4.08", "4.08.01", "<"),
            ("3.2.1.9.8144", "3.2", ">"),
            ("3.2", "3.2.1.9.8144", "<"),
            ("1.2", "2.1", "<"),
            ("2.1", "1.2", ">"),
            ("5.6.7", "5.6.7", "="),
            ("1.01.1", "1.1.1", "="),
            ("1.1.1", "1.01.1", "="),
            ("1", "1.0", "="),
            ("1.0", "1", "="),
            ("1.0.2.0", "1.0.2", "="),
            ("1..0", "1.0", "="),
            ("1.0", "1..0", "="),
        ],
    )
    def test_vercomp(self, bash, ver1, ver2, result):
        output = assert_bash_exec(
            bash,
            f"_comp_cmd_rsync__vercomp {ver1} {ver2}; echo $?",
            want_output=True,
        ).strip()

        if result == "=":
            assert output == "0"
        elif result == ">":
            assert output == "1"
        elif result == "<":
            assert output == "2"
        else:
            raise Exception(f"Unsupported comparison result: {result}")

    def test_remote_path_with_spaces(self, bash):
        assert_bash_exec(bash, "ssh() { echo 'spaces in filename.txt'; }")
        completion = assert_complete(bash, "rsync remote_host:spaces")
        assert_bash_exec(bash, "unset -f ssh")
        assert (
            completion == r"\ in\ filename.txt"
            or completion == r"\\\ in\\\ filename.txt"
        )

    @pytest.mark.complete(r"rsync -na spaced\ ", cwd="scp")
    def test_local_path_with_spaces(self, completion):
        """This function tests xfunc _comp_xfunc_scp_compgen_local_files, which
        is defined in completions/ssh, through the rsync interface.  We reuse
        the fixture directory for the test of the scp completion.

        The expected result depends on the rsync version, so we check the
        result if it matches either one of two possible expected results.

        """
        assert completion == r"\ conf" or completion == r"\\\ conf"
