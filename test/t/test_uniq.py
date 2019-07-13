import pytest


class TestUniq:
    @pytest.mark.complete("uniq --", require_longopt=True)
    def test_1(self, completion):
        assert completion
