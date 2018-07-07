import pytest


class TestObjdump(object):

    @pytest.mark.complete("objdump ")
    def test_1(self, completion):
        assert completion.list
