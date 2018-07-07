import pytest


class TestCowsay(object):

    @pytest.mark.complete("cowsay ")
    def test_1(self, completion):
        assert completion.list
