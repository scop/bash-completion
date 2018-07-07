import pytest


class TestAptitude(object):

    @pytest.mark.complete("aptitude ")
    def test_1(self, completion):
        assert completion.list
