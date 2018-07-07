import pytest


class TestRmdir(object):

    @pytest.mark.complete("rmdir ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("rmdir shared/default/")
    def test_2(self, completion):
        assert completion.list == ["bar bar.d/", "foo.d/"]
