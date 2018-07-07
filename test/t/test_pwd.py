import pytest


class TestPwd(object):

    @pytest.mark.complete("pwd -")
    def test_1(self, completion):
        assert completion.list
