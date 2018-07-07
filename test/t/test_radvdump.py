import pytest


class TestRadvdump(object):

    @pytest.mark.complete("radvdump ")
    def test_1(self, completion):
        assert completion.list
