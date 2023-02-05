import pytest


class TestKillall:
    # "p": Assume our process name completion runs ps and at least it is shown
    @pytest.mark.complete("killall p")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("killall --signal ")
    def test_2(self, completion):
        assert all(x in completion for x in "INT KILL TERM".split())

    @pytest.mark.complete("killall ")
    def test_3(self, completion):
        assert "command=" not in completion

    @pytest.mark.complete("killall -", require_cmd=True)
    def test_4(self, completion):
        assert completion
