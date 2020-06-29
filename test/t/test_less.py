import pytest


class TestLess:
    @pytest.mark.complete("less --", require_longopt=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("less --", require_longopt=True)
    def test_no_dashdashdash(self, completion):
        assert all(not x.startswith("---") for x in completion)
