import pytest


class TestCo(object):

    @pytest.mark.complete("co ")
    def test_1(self, completion):
        assert completion.list
