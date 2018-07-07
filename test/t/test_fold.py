import pytest


class TestFold(object):

    @pytest.mark.complete("fold --",
                          skipif="! fold --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
