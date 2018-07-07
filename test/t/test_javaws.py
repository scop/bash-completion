import pytest


class TestJavaws(object):

    @pytest.mark.complete("javaws ")
    def test_1(self, completion):
        assert completion.list
