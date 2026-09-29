import pytest


class TestSha512sum:
    @pytest.mark.complete("sha512sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
