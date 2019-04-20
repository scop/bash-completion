import pytest


class TestAspell:
    @pytest.mark.complete("aspell ")
    def test_1(self, completion):
        assert completion
