import pytest


class TestFunction(object):

    @pytest.mark.complete("function _parse_")
    def test_1(self, completion):
        assert completion.list
