import pytest


class TestGroupmems(object):

    @pytest.mark.complete("groupmems -")
    def test_1(self, completion):
        assert completion.list
