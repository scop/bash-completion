import pytest


class TestKcov:
    @pytest.mark.complete("kcov ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("kcov --exclude-patter")
    def test_2(self, completion):
        assert completion == "--exclude-pattern="
        assert completion.endswith("=")

    @pytest.mark.complete("kcov -l 42,")
    def test_3(self, completion):
        assert completion
