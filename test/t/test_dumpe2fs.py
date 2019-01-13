import pytest


class TestDumpe2fs:

    @pytest.mark.complete("dumpe2fs ")
    def test_1(self, completion):
        assert completion
