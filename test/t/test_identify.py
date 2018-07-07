import pytest


class TestIdentify(object):

    @pytest.mark.complete("identify -")
    def test_1(self, completion):
        assert completion.list
