import pytest


class TestMuninRun(object):

    @pytest.mark.complete("munin-run -")
    def test_1(self, completion):
        assert completion.list
