import pytest


class TestNm:
    @pytest.mark.complete("nm ")
    def test_1(self, completion):
        assert completion
