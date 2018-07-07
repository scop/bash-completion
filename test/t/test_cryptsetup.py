import pytest


class TestCryptsetup(object):

    @pytest.mark.complete("cryptsetup ")
    def test_1(self, completion):
        assert completion.list
