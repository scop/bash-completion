import pytest


class TestPkgadd:
    @pytest.mark.complete("pkgadd ")
    def test_1(self, completion):
        assert completion
