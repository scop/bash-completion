import pytest


class TestXxd:
    @pytest.mark.complete("xxd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xxd -")
    def test_2(self, completion):
        assert completion
