import pytest


class TestPwdx(object):

    @pytest.mark.complete("pwdx ")
    def test_1(self, completion):
        assert completion.list
