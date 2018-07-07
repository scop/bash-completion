import pytest


class TestRunuser(object):

    @pytest.mark.complete("runuser ")
    def test_1(self, completion):
        assert completion.list
