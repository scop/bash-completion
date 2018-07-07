import pytest


class TestMktemp(object):

    @pytest.mark.complete("mktemp -")
    def test_1(self, completion):
        assert completion.list
