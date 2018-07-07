import pytest


class TestNl(object):

    @pytest.mark.complete("nl ")
    def test_1(self, completion):
        assert completion.list
