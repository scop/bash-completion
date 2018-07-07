import pytest


class TestGcj(object):

    @pytest.mark.complete("gcj ")
    def test_1(self, completion):
        assert completion.list
