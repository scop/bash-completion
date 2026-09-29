import pytest


class TestPwd:
    @pytest.mark.complete("pwd -", require_cmd=True)
    def test_1(self, completion):
        assert completion
