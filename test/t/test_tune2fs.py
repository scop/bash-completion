import pytest


class TestTune2fs:
    @pytest.mark.complete("tune2fs ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tune2fs -", require_cmd=True)
    def test_2(self, completion):
        assert completion
