import pytest


class TestCsplit(object):

    @pytest.mark.complete("csplit ")
    def test_1(self, completion):
        assert completion.list
