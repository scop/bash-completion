import pytest


@pytest.mark.bashcomp(cmd="pm-is-supported")
class TestPmIsSupported:
    @pytest.mark.complete("pm-is-supported -")
    def test_1(self, completion):
        assert completion
