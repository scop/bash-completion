import pytest


class TestBase64(object):

    @pytest.mark.complete("base64 ")
    def test_1(self, completion):
        assert completion.list
