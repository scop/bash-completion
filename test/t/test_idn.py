import pytest


class TestIdn(object):

    @pytest.mark.complete("idn -")
    def test_1(self, completion):
        assert completion.list
