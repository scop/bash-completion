import pytest


class TestXmms(object):

    @pytest.mark.complete("xmms --")
    def test_1(self, completion):
        assert completion.list
