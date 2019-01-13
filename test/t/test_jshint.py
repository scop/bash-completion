import pytest


class TestJshint:

    @pytest.mark.complete("jshint ")
    def test_1(self, completion):
        assert completion
