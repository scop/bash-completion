import pytest


class TestUnits(object):

    @pytest.mark.complete("units --",
                          skipif="! units --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
