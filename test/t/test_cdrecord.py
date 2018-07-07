import pytest


class TestCdrecord(object):

    @pytest.mark.complete("cdrecord -d")
    def test_1(self, completion):
        assert completion.list
