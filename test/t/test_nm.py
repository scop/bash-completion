import pytest


class TestNm:
    @pytest.mark.complete("nm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("nm -", require_cmd=True)
    def test_options(self, completion):
        assert completion
