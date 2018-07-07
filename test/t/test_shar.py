import pytest


class TestShar(object):

    @pytest.mark.complete("shar --")
    def test_1(self, completion):
        assert completion.list
