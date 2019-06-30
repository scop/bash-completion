import pytest


@pytest.mark.bashcomp(cmd="sbcl-mt")
class TestSbclMt:
    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("sbcl-mt shared/default/")
    def test_1(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo foo.d/"]
