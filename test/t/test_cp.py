import pytest


class TestCp:
    @pytest.mark.complete("cp ")
    def test_1(self, completion):
        assert completion
