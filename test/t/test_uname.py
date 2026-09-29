import pytest


class TestUname:
    @pytest.mark.complete("uname --", require_longopt=True)
    def test_1(self, completion):
        assert completion
