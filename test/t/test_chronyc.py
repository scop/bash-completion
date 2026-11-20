import pytest


class TestChronyc:
    @pytest.mark.complete("chronyc ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chronyc -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("chronyc sources ")
    def test_sources(self, completion):
        assert completion == "-v"

    @pytest.mark.complete("chronyc nonexistent-command ")
    def test_unknown_command(self, completion):
        assert not completion
