import pytest


class TestObjcopy:
    @pytest.mark.complete("objcopy ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("objcopy -", require_cmd=True)
    def test_options(self, completion):
        assert completion
