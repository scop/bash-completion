import pytest


@pytest.mark.bashcomp(cmd="freeciv-server")
class TestFreecivServer:
    @pytest.mark.complete("freeciv-server -")
    def test_1(self, completion):
        assert completion
