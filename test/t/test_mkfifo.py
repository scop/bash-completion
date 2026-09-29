import pytest


class TestMkfifo:
    @pytest.mark.complete("mkfifo ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mkfifo -", require_longopt=True)
    def test_options(self, completion):
        assert completion
