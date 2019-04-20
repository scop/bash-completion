import pytest


class TestReadonly:
    @pytest.mark.complete("readonly BASH_ARG")
    def test_1(self, completion):
        assert completion
