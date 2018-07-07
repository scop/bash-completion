import pytest


class TestJar(object):

    @pytest.mark.complete("jar ")
    def test_1(self, completion):
        assert completion.list
