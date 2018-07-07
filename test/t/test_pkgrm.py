import pytest


class TestPkgrm(object):

    @pytest.mark.complete("pkgrm ")
    def test_1(self, completion):
        assert completion.list
