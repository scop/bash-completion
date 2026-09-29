import pytest


class TestObjdump:
    @pytest.mark.complete("objdump ")
    def test_1(self, completion):
        assert completion
