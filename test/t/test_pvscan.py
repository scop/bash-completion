import pytest


class TestPvscan(object):

    @pytest.mark.complete("pvscan --")
    def test_1(self, completion):
        assert completion.list
