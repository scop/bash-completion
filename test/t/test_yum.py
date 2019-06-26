import pytest


class TestYum:
    @pytest.mark.complete("yum -", require_cmd=True)
    def test_1(self, completion):
        assert completion
