import pytest


class TestRmdir:

    @pytest.mark.complete("rmdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rmdir shared/default/")
    def test_2(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]
