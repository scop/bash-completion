import pytest


class TestEnscript(object):

    @pytest.mark.complete("enscript --")
    def test_1(self, completion):
        assert completion.list
