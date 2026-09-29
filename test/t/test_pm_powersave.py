import pytest


@pytest.mark.bashcomp(cmd="pm-powersave")
class TestPmPowersave:
    @pytest.mark.complete("pm-powersave ")
    def test_1(self, completion):
        assert completion
