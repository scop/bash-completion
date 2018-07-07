import pytest


class TestQrunner(object):

    @pytest.mark.complete("qrunner -")
    def test_1(self, completion):
        assert completion.list
