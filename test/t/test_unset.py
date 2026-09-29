import pytest


class TestUnset:
    @pytest.mark.complete("unset BASH_ARG")
    def test_1(self, completion):
        assert completion
