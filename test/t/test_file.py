import pytest


class TestFile:
    @pytest.mark.complete("file ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("file -", require_cmd=True)
    def test_2(self, completion):
        assert completion
