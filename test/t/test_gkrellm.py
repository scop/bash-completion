import pytest


class TestGkrellm:

    @pytest.mark.complete("gkrellm -")
    def test_1(self, completion):
        assert completion.list
