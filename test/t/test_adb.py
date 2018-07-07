import pytest


class TestAdb(object):

    @pytest.mark.complete("adb ")
    def test_1(self, completion):
        assert completion.list
