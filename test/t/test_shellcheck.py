import pytest


class TestShellcheck:
    @pytest.mark.complete("shellcheck ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck --format=")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("shellcheck -s ")
    def test_4(self, completion):
        assert "bash" in completion
