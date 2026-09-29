import pytest


class TestSitecopy:
    @pytest.mark.complete("sitecopy --", require_cmd=True)
    def test_1(self, completion):
        assert completion
