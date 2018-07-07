import pytest


class TestTr(object):

    @pytest.mark.complete("tr --",
                          skipif="! tr --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
