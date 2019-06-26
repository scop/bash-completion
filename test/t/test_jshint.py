import pytest


class TestJshint:
    @pytest.mark.complete("jshint ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("jshint -", require_cmd=True)
    def test_2(self, completion):
        assert completion
