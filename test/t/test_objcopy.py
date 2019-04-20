import pytest


class TestObjcopy:
    @pytest.mark.complete("objcopy ")
    def test_1(self, completion):
        assert completion
