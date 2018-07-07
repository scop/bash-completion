import pytest


class TestXzdec(object):

    @pytest.mark.complete("xzdec ")
    def test_1(self, completion):
        assert completion.list
