import pytest


class TestCfagent(object):

    @pytest.mark.complete("cfagent -")
    def test_1(self, completion):
        assert completion.list
