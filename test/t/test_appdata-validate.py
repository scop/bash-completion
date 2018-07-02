import pytest


class Test(object):

    @pytest.mark.complete("appdata-validate ")
    def test_(self, completion):
        assert completion.list
