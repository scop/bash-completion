import pytest


class TestTr:
    @pytest.mark.complete("tr --", xfail="! tr --help &>/dev/null")
    def test_1(self, completion):
        assert completion
