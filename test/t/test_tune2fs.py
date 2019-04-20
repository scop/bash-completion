import pytest


class TestTune2fs:
    @pytest.mark.complete("tune2fs ")
    def test_1(self, completion):
        assert completion
