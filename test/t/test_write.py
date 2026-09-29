import pytest


class TestWrite:
    @pytest.mark.complete("write roo")
    def test_1(self, completion):
        assert completion == "t" or "root" in completion
