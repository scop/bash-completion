import pytest


class TestAutorpm(object):

    @pytest.mark.complete("autorpm ")
    def test_1(self, completion):
        assert completion.list
