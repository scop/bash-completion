import pytest


@pytest.mark.bashcomp(cmd="munin-run")
class TestMuninRun:
    @pytest.mark.complete("munin-run -")
    def test_1(self, completion):
        assert completion
