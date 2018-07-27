import pytest


class TestWine:

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("wine ", cwd="shared/default")
    def test_1(self, completion):
        assert completion.list == ["bar bar.d/", "foo.d/"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("wine notepad ", cwd="shared/default")
    def test_2(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo.d/"]
