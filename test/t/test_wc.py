import pytest


class TestWc(object):

    @pytest.mark.complete("wc --",
                          skipif="! wc --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
