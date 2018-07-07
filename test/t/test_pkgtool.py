import pytest


class TestPkgtool(object):

    @pytest.mark.complete("pkgtool -")
    def test_1(self, completion):
        assert completion.list
