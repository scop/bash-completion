import pytest


class TestGkrellm(object):

    @pytest.mark.complete("gkrellm -")
    def test_1(self, completion):
        assert completion.list
