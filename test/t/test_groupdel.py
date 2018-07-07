import pytest


class TestGroupdel(object):

    @pytest.mark.complete("groupdel ")
    def test_1(self, completion):
        assert completion.list
