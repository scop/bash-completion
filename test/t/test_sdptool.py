import pytest


class TestSdptool(object):

    @pytest.mark.complete("sdptool ")
    def test_1(self, completion):
        assert completion.list
