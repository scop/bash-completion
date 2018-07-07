import pytest


class TestMkfifo(object):

    @pytest.mark.complete("mkfifo ")
    def test_1(self, completion):
        assert completion.list
