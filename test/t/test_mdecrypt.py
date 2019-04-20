import pytest


class TestMdecrypt:
    @pytest.mark.complete("mdecrypt ")
    def test_1(self, completion):
        assert completion
