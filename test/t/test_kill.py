import pytest


class TestKill:
    @pytest.mark.complete("kill 1", xfail="! type ps &>/dev/null")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("kill -s ")
    def test_2(self, completion):
        assert all(x in completion for x in "HUP QUIT".split())

    @pytest.mark.complete("kill -")
    def test_3(self, completion):
        assert all("-%s" % x in completion for x in "l s ABRT USR1".split())
