import pytest


class TestGpg2:
    @pytest.mark.complete("gpg2 --h", require_cmd=True)
    def test_1(self, completion):
        assert completion
