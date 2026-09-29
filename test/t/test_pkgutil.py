import pytest


class TestPkgutil:
    @pytest.mark.complete("pkgutil ")
    def test_1(self, completion):
        assert completion
