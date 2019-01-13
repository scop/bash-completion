import pytest


class TestCryptsetup:

    @pytest.mark.complete("cryptsetup ")
    def test_1(self, completion):
        assert completion
