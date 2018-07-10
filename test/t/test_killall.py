import pytest


class TestKillall(object):

    # "p": Assume our process name completion runs ps and at least it is shown
    @pytest.mark.complete("killall p")
    def test_1(self, completion):
        assert completion.list
