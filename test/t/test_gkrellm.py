import pytest


class Test(object):

    @pytest.mark.complete("gkrellm -")
    def test_dash(self, completion):
        assert completion.list
