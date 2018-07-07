import pytest


class TestUniq(object):

    @pytest.mark.complete("uniq --",
                          skipif="! uniq --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
