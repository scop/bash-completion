import pytest


class TestWrite:
    @pytest.mark.complete("write root")
    def test_1(self, completion):
        assert "root" in completion
