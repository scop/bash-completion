import pytest


class TestEbtables(object):

    @pytest.mark.complete("ebtables -")
    def test_1(self, completion):
        assert completion.list
