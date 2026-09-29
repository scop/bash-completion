import pytest


class TestMedusa:
    @pytest.mark.complete("medusa -", require_cmd=True)
    def test_1(self, completion):
        assert completion
