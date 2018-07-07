import pytest


class TestMinicom(object):

    @pytest.mark.complete("minicom -")
    def test_1(self, completion):
        assert completion.list
