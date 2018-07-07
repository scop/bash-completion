import pytest


class TestObjcopy(object):

    @pytest.mark.complete("objcopy ")
    def test_1(self, completion):
        assert completion.list
