import pytest


class TestChroot:
    @pytest.mark.complete("chroot ")
    def test_1(self, completion):
        assert completion
