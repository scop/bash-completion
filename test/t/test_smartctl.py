import pytest


class TestSmartctl(object):

    @pytest.mark.complete("smartctl --")
    def test_1(self, completion):
        assert completion.list
