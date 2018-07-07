import pytest


class TestFilefrag(object):

    @pytest.mark.complete("filefrag ")
    def test_1(self, completion):
        assert completion.list
