import pytest


class TestBadblocks:
    @pytest.mark.complete("badblocks ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("badblocks -", require_cmd=True)
    def test_2(self, completion):
        assert completion
        assert all(x not in completion for x in "-w -X".split())
