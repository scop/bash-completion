import pytest


class TestPvs:

    @pytest.mark.complete("pvs --",
                          skipif="! pvs --help &>/dev/null")
    def test_1(self, completion):
        assert completion
