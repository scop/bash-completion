import pytest


class TestMknod:
    @pytest.mark.complete("mknod ")
    def test_1(self, completion):
        assert completion
