import pytest


class TestSha384sum:
    @pytest.mark.complete("sha384sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
