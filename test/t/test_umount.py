import pytest


class TestUmount:
    @pytest.mark.complete("umount ")
    def test_1(self, completion):
        assert completion
