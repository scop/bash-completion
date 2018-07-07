import pytest


class TestStrip(object):

    @pytest.mark.complete("strip --")
    def test_1(self, completion):
        assert completion.list
