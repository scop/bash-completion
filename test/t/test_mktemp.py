import pytest


class Test(object):

    @pytest.mark.complete("mktemp -")
    def test_dash(self, completion):
        assert completion.list
