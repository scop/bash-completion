import pytest


class TestCdrecord:
    @pytest.mark.complete("cdrecord -d")
    def test_1(self, completion):
        assert completion
