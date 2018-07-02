import pytest


class Test(object):

    @pytest.mark.complete("mdadm ")
    def test_(self, completion):
        assert completion.list
