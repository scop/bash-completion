import pytest


class TestSbclMt(object):

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("sbcl-mt shared/default/")
    def test_1(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo foo.d/"]
