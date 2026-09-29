import pytest


class TestPkgadd:
    # require_cmd is not strictly true here, but...
    @pytest.mark.complete("pkgadd ", require_cmd=True)
    def test_1(self, completion):
        assert completion
