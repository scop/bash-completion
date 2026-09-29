import pytest


class TestMknod:
    @pytest.mark.complete("mknod ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mknod -", require_longopt=True)
    def test_options(self, completion):
        assert completion
