import pytest


class TestDumpe2fs(object):

    @pytest.mark.complete("dumpe2fs ")
    def test_1(self, completion):
        assert completion.list
