import pytest


class TestPidof:

    # "p": Assume that our process name completion runs ps
    @pytest.mark.complete("pidof p")
    def test_1(self, completion):
        assert completion.list
