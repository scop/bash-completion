import pytest


class TestRcsdiff(object):

    @pytest.mark.complete("rcsdiff ")
    def test_1(self, completion):
        assert completion.list
