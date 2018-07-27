import pytest


@pytest.mark.bashcomp(ignore_env=r"^-declare -f _tar$")
class TestTar:

    @pytest.mark.complete("tar ")
    def test_1(self, completion):
        assert completion.list

    # Test "f" when mode is not as first option
    @pytest.mark.complete("tar zfc ", cwd="tar")
    def test_2(self, completion):
        assert completion.list == "dir/ dir2/".split()

    @pytest.mark.complete("tar cf ", cwd="tar")
    def test_3(self, completion):
        assert completion.list == "dir/ dir2/".split()

    @pytest.mark.complete("tar tf archive.tar.xz dir/file", cwd="tar")
    def test_4(self, completion):
        assert completion.list == "dir/fileA dir/fileB dir/fileC".split()

    @pytest.mark.complete("tar cTfvv NOT_EXISTS DONT_CREATE.tar ", cwd="tar")
    def test_5(self, completion):
        assert completion.list == \
            "archive.tar.xz dir/ dir2/ escape.tar".split()

    @pytest.mark.complete("tar xvf ", cwd="tar")
    def test_6(self, completion):
        assert completion.list == \
            "archive.tar.xz dir/ dir2/ escape.tar".split()
