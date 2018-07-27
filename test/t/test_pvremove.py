import pytest


class TestPvremove:

    @pytest.mark.complete("pvremove --",
                          skipif="! pvremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
