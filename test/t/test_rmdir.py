import pytest


class TestRmdir:
    @pytest.mark.complete("rmdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("/bin/rmdir shared/default/")
    def test_2(self, completion):
        """Should complete dirs only, also when invoked using full path."""
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("rmdir -", require_cmd=True)
    def test_options(self, completion):
        assert completion
