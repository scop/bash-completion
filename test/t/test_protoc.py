import pytest


class TestProtoc(object):

    @pytest.mark.complete("protoc ")
    def test_1(self, completion):
        assert completion.list
