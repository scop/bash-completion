import pytest


class TestIdn:
    @pytest.mark.complete("idn -", require_cmd=True)
    def test_1(self, completion):
        assert completion
