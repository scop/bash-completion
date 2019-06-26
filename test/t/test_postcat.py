import pytest


class TestPostcat:
    @pytest.mark.complete("postcat ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("postcat -", require_cmd=True)
    def test_2(self, completion):
        assert completion
