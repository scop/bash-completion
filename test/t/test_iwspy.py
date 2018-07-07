import pytest


class TestIwspy(object):

    @pytest.mark.complete("iwspy --")
    def test_1(self, completion):
        assert completion.list
