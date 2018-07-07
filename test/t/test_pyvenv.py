import pytest


class TestPyvenv(object):

    @pytest.mark.complete("pyvenv ")
    def test_1(self, completion):
        assert completion.list
