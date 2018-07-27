import pytest


class TestPyflakes:

    @pytest.mark.complete("pyflakes ")
    def test_1(self, completion):
        assert completion.list
