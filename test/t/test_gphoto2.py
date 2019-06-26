import pytest


class TestGphoto2:
    @pytest.mark.complete("gphoto2 --", require_cmd=True)
    def test_1(self, completion):
        assert completion
