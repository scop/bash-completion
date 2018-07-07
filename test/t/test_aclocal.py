import pytest


class TestAclocal(object):

    @pytest.mark.complete("aclocal ")
    def test_1(self, completion):
        assert completion.list
