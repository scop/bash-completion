import pytest


class TestLdapadd(object):

    @pytest.mark.complete("ldapadd -")
    def test_1(self, completion):
        assert completion.list
