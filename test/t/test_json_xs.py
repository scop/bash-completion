import pytest


class TestJsonXs(object):

    @pytest.mark.complete("json_xs ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("json_xs -")
    def test_2(self, completion):
        assert completion.list
