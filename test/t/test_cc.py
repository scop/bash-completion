import pytest


class TestCc(object):

    @pytest.mark.complete("cc ")
    def test_1(self, completion):
        assert completion.list
