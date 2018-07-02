import pytest


class Test(object):

    @pytest.mark.complete("gpg2 --h")
    def test_h(self, completion):
        assert completion.list
