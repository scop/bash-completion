import pytest


class TestStream(object):

    @pytest.mark.complete("stream ")
    def test_1(self, completion):
        assert completion.list
