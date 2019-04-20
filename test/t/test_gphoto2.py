import pytest


class TestGphoto2:
    @pytest.mark.complete("gphoto2 --")
    def test_1(self, completion):
        assert completion
