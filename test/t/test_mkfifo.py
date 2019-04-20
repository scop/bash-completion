import pytest


class TestMkfifo:
    @pytest.mark.complete("mkfifo ")
    def test_1(self, completion):
        assert completion
