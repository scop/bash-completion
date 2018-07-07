import pytest


class TestIwpriv(object):

    @pytest.mark.complete("iwpriv --")
    def test_1(self, completion):
        assert completion.list
