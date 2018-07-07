import pytest


class TestEog(object):

    @pytest.mark.complete("eog ")
    def test_1(self, completion):
        assert completion.list
