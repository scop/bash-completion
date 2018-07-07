import pytest


class TestAlpine(object):

    @pytest.mark.complete("alpine -")
    def test_1(self, completion):
        assert completion.list
