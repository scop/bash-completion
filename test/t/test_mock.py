import pytest


class TestMock(object):

    @pytest.mark.complete("mock ")
    def test_1(self, completion):
        assert completion.list
