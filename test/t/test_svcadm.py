import pytest


class Test(object):

    @pytest.mark.complete("svcadm ")
    def test_(self, completion):
        assert completion.list
