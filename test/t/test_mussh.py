import pytest


class TestMussh(object):

    @pytest.mark.complete("mussh -")
    def test_1(self, completion):
        assert completion.list
