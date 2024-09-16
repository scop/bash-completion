import pytest


class TestSlabtop:
    @pytest.mark.complete("slabtop --", require_cmd=True)
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("slabtop --sort ", require_cmd=True)
    def test_sort_arg(self, completion):
        assert completion
