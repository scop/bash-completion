import pytest


class TestPrelink:
    @pytest.mark.complete("prelink ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("prelink -", require_cmd=True)
    def test_2(self, completion):
        assert completion
