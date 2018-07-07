import pytest


class TestPwgen(object):

    @pytest.mark.complete("pwgen -")
    def test_1(self, completion):
        assert completion.list
