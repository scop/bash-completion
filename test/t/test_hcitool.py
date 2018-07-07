import pytest


class TestHcitool(object):

    @pytest.mark.complete("hcitool ")
    def test_1(self, completion):
        assert completion.list
