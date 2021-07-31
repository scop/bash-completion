import pytest


class TestTree:
    @pytest.mark.complete("tree ", cwd="shared/default")
    def test_basic(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("tree --fromfile ", cwd="shared/default")
    def test_fromfile(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("tree -", require_cmd=True)
    def test_options(self, completion):
        assert completion
