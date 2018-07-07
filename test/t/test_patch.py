import pytest


class TestPatch(object):

    @pytest.mark.complete("patch ")
    def test_1(self, completion):
        assert completion.list
