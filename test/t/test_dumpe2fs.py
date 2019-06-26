import pytest


class TestDumpe2fs:
    @pytest.mark.complete("dumpe2fs ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dumpe2fs -", require_cmd=True)
    def test_2(self, completion):
        assert completion
