import pytest


class Test(object):

    @pytest.mark.complete("pwdx ")
    def test_(self, completion):
        assert completion.list
