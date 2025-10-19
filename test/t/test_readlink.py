import pytest


class TestReadlink:
    @pytest.mark.complete("readlink ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("readlink -", require_longopt=True)
    def test_options(self, completion):
        assert completion
