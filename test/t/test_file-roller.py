import pytest


class TestFileRoller(object):

    @pytest.mark.complete("file-roller ")
    def test_1(self, completion):
        assert completion.list
