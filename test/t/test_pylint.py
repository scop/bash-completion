import pytest


class TestPylint:
    @pytest.mark.complete("pylint --v")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pylint --confidence=HIGH,")
    def test_2(self, completion):
        assert completion
