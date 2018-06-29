import pytest


class Test(object):

    @pytest.mark.complete("readonly BASH_ARG")
    def test_BASH_ARG(self, completion):
        assert completion.list
