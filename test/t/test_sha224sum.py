import pytest


class TestSha224sum:
    @pytest.mark.complete("sha224sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
