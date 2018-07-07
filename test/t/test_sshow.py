import pytest


class TestSshow(object):

    @pytest.mark.complete("sshow -")
    def test_1(self, completion):
        assert completion.list
