import pytest


class TestKill:

    @pytest.mark.complete("kill 1", skipif="! type ps &>/dev/null")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("kill -s ")
    def test_2(self, completion):
        for arg in "HUP QUIT".split():
            assert arg in completion.list

    @pytest.mark.complete("kill -")
    def test_3(self, completion):
        for arg in "l s ABRT USR1".split():
            assert "-%s" % arg in completion.list
