import pytest


class TestRtcwake(object):

    @pytest.mark.complete("rtcwake ")
    def test_1(self, completion):
        assert completion.list
