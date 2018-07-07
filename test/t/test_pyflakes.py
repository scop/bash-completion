import pytest


class TestPyflakes(object):

    @pytest.mark.complete("pyflakes ")
    def test_1(self, completion):
        assert completion.list
