import pytest


@pytest.mark.bashcomp(
    cmd="plague-client",
)
class TestPlagueClient(object):

    @pytest.mark.complete("plague-client ")
    def test_1(self, completion):
        assert completion.list
