import pytest


class TestExport:
    @pytest.mark.complete("export BASH")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("export -n BASH")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("export -p ")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("export FOO=", cwd="shared/default")
    def test_4(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("export FOO=f", cwd="shared/default")
    def test_5(self, completion):
        assert completion == ["foo", "foo.d/"]

    @pytest.mark.complete("export -fn _ex")
    def test_6(self, completion):
        assert "_expand" in completion
        assert "_export" in completion

    @pytest.mark.complete(r"export FOO=$BASH")
    def test_7(self, completion):
        assert completion

    @pytest.mark.complete("export -", require_cmd=True)
    def test_8(self, completion):
        assert completion
