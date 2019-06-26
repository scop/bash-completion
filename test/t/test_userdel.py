import pytest


class TestUserdel:
    @pytest.mark.complete("userdel -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("userdel root")
    def test_2(self, completion):
        assert "root" in completion
