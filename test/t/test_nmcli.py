import pytest


class Test(object):

    @pytest.mark.complete("nmcli ")
    def test_(self, completion):
        assert completion.list
