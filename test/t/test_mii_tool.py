import pytest


@pytest.mark.bashcomp(
    cmd="mii-tool",
)
class TestMiiTool(object):

    @pytest.mark.complete("mii-tool ")
    def test_1(self, completion):
        assert completion.list
