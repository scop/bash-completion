import pytest


class TestRtcwake:
    @pytest.mark.complete("rtcwake ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rtcwake -")
    def test_2(self, completion):
        assert completion
