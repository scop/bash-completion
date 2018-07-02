import pytest


class Test(object):

    @pytest.mark.complete("postcat ")
    def test_(self, completion):
        assert completion.list
