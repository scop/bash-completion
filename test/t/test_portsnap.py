import pytest


class TestPortsnap(object):

    @pytest.mark.complete("portsnap ")
    def test_1(self, completion):
        assert completion.list
