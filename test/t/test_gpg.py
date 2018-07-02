import pytest


class Test(object):

    @pytest.mark.complete("gpg ")
    def test_(self, completion):
        assert completion.list
