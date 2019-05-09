import pytest


@pytest.mark.bashcomp(cmd="mii-tool")
class TestMiiTool:
    @pytest.mark.complete("mii-tool ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mii-tool -")
    def test_2(self, completion):
        assert completion
