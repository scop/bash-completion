import pytest


class TestPushd(object):

    @pytest.mark.complete("pushd ")
    def test_1(self, completion):
        assert completion.list
