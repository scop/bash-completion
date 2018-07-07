import pytest


class TestSvk(object):

    @pytest.mark.complete("svk ")
    def test_1(self, completion):
        assert completion.list
