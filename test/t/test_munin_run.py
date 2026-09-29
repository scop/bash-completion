import pytest


@pytest.mark.bashcomp(cmd="munin-run")
class TestMuninRun:
    @pytest.mark.complete("munin-run -", require_cmd=True)
    def test_1(self, completion):
        assert completion
