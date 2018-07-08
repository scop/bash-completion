import pytest


@pytest.mark.bashcomp(
    cmd="invoke-rc.d",
)
class TestInvokeRcD(object):

    @pytest.mark.complete("invoke-rc.d ")
    def test_1(self, completion):
        assert completion.list
