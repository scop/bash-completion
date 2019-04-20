import pytest


class TestLintian:
    @pytest.mark.complete("lintian --")
    def test_1(self, completion):
        assert completion
