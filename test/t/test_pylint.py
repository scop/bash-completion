import pytest


class TestPylint:
    @pytest.mark.complete("pylint --v", require_cmd=True, require_longopt=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pylint --confidence=HIGH,")
    def test_2(self, completion):
        assert completion
