import pytest


class TestTune2fs(object):

    @pytest.mark.complete("tune2fs ")
    def test_1(self, completion):
        assert completion.list
