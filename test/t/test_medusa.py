import pytest


class TestMedusa(object):

    @pytest.mark.complete("medusa -")
    def test_1(self, completion):
        assert completion.list
