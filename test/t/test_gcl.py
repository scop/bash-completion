import pytest


class TestGcl(object):

    @pytest.mark.complete("gcl ")
    def test_1(self, completion):
        assert completion.list
