import pytest


class TestIw:
    @pytest.mark.complete("iw ", require_cmd=True)
    def test_1(self, completion):
        assert all(x in completion for x in "commands dev event features help list phy reg wdev".split())

    @pytest.mark.complete("iw d", require_cmd=True)
    def test_2(self, completion):
        assert completion == "dev"
