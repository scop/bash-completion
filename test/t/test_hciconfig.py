import pytest


class TestHciconfig(object):

    @pytest.mark.complete("hciconfig ")
    def test_1(self, completion):
        assert completion.list
