import pytest


class TestGpg:
    @pytest.mark.complete("gpg ")
    def test_1(self, completion):
        assert completion
