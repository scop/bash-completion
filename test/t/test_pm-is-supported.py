import pytest


class TestPmIsSupported(object):

    @pytest.mark.complete("pm-is-supported -")
    def test_1(self, completion):
        assert completion.list
