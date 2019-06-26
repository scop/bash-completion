import pytest


class TestPwgen:
    @pytest.mark.complete("pwgen -", require_cmd=True)
    def test_1(self, completion):
        assert completion
