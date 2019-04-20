import pytest


@pytest.mark.bashcomp(cmd="plague-client")
class TestPlagueClient:
    @pytest.mark.complete("plague-client ")
    def test_1(self, completion):
        assert completion
