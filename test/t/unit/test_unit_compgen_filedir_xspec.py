import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=|^[-+]_comp_xspecs=")
class TestUnitFiledirXspec:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_comp_xspecs[xspec1]='!*.txt'; "
            "_comp_xspecs[xspec2]=; "
            "_comp_xspecs[xspec4]='*.txt'; "
            "complete -F _filedir_xspec xspec{1..4}",
        )

    @pytest.mark.complete("xspec1 ", cwd="_filedir_xspec")
    def test_1(self, functions, completion):
        """Test the pattern for an extension"""
        assert completion == sorted("a.txt b.TXT".split())

    @pytest.mark.complete("xspec2 ", cwd="_filedir_xspec")
    def test_2(self, functions, completion):
        """Test an empty _comp_xspecs entry"""
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    @pytest.mark.complete("xspec3 ", cwd="_filedir_xspec")
    def test_3(self, functions, completion):
        """Test an unset _comp_xspecs entry"""
        assert completion == sorted("a.txt b.TXT c.dat d.bin".split())

    @pytest.mark.complete("xspec4 ", cwd="_filedir_xspec")
    def test_4(self, functions, completion):
        """Test an exclusion pattern"""
        assert completion == sorted("c.dat d.bin".split())


@pytest.mark.bashcomp(cmd=None)
class TestDefaultFiledirXspec:
    @pytest.fixture(scope="class")
    def files(self, tmp_path_factory):
        directory = tmp_path_factory.mktemp("bash-completion.xspec.")
        for name in ("notes.txt", "photo.gif", "two words.txt"):
            (directory / name).touch()
        (directory / "subdir").mkdir()
        return directory

    @pytest.mark.parametrize("command", ("ee", "qiv", "xv"))
    def test_filenames(self, bash, files, command):
        completion = assert_complete(bash, command + " ", cwd=files)
        expected = ["photo.gif", "subdir/"]
        if command == "ee":
            expected = ["notes.txt", "photo.gif", "subdir/", "two words.txt"]
        assert completion == expected

    @pytest.mark.parametrize(
        "word, suffix",
        (("no", "tes.txt"), ("tw", r"o\ words.txt"), ("su", "bdir/")),
    )
    def test_editor_prefix(self, bash, files, word, suffix):
        assert assert_complete(bash, "ee " + word, cwd=files) == suffix

    @pytest.mark.parametrize("command", ("ee", "qiv", "xv"))
    def test_dedicated_completion(self, bash, files, tmp_path, command):
        completions = tmp_path / "completions"
        completions.mkdir()
        (completions / (command + ".bash")).write_text(
            "complete -W dedicated-completion " + command + "\n"
        )
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("BASH_COMPLETION_USER_DIR", str(tmp_path))
            assert_bash_exec(bash, "complete -r " + command + " || :")
            try:
                completion = assert_complete(bash, command + " ", cwd=files)
                assert completion == "dedicated-completion"
            finally:
                assert_bash_exec(bash, "complete -r " + command)
