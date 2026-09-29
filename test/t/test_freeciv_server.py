import pytest


@pytest.mark.bashcomp(cmd="freeciv-server")
class TestFreecivServer:
    @pytest.mark.complete("freeciv-server -", require_cmd=True)
    def test_1(self, completion):
        assert completion
