import pytest


class TestRadvdump:
    @pytest.mark.complete("radvdump ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("radvdump -")
    def test_2(self, completion):
        assert completion
