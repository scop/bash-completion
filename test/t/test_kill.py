import pytest


class TestKill(object):

    @pytest.mark.complete("kill 1", skipif="! type ps &>/dev/null")
    def test_1(self, completion):
        assert completion.list
