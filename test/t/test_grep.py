import pytest


class TestGrep:

    @pytest.mark.complete("grep --")
    def test_1(self, completion):
        assert completion
