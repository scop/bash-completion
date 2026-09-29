import pytest


class TestCiptool:
    @pytest.mark.complete("ciptool ")
    def test_1(self, completion):
        assert completion
