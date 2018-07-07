import pytest


class TestSbopkg(object):

    @pytest.mark.complete("sbopkg -")
    def test_1(self, completion):
        assert completion.list
