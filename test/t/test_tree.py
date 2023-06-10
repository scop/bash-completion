import pytest


class TestTree:
    @pytest.mark.complete("tree ", cwd="shared/default")
    def test_basic(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("tree --fromfile ", cwd="shared/default")
    def test_fromfile(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete(
        "tree -",
        require_cmd=True,
        xfail="! tree --help 2>&1 | command grep -qF -- ' -'",
    )
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("tree --sort=", require_cmd=True)
    def test_equals_sign_split(self, completion):
        assert completion
