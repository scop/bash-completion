import pytest


class TestWodim(object):

    @pytest.mark.complete("wodim ")
    def test_1(self, completion):
        assert completion.list
