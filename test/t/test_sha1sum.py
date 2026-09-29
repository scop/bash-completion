import pytest


class TestSha1sum:
    @pytest.mark.complete("sha1sum --", require_longopt=True)
    def test_1(self, completion):
        assert completion
