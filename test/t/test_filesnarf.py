import pytest


class TestFilesnarf(object):

    @pytest.mark.complete("filesnarf -")
    def test_1(self, completion):
        assert completion.list
