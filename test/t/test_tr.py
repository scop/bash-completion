import pytest


class TestTr:
    @pytest.mark.complete("tr --", require_longopt=True)
    def test_1(self, completion):
        assert completion
