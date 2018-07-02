import pytest


class Test(object):

    @pytest.mark.complete("e2label ")
    def test_(self, completion):
        assert completion.list
