import pytest


class TestGpg2:
    @pytest.mark.complete("gpg2 --h")
    def test_1(self, completion):
        assert completion
