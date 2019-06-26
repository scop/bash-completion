import pytest


class TestHost:
    @pytest.mark.complete("host -", require_cmd=True)
    def test_1(self, completion):
        assert completion
