import pytest


class TestOptipng:

    @pytest.mark.complete("optipng ")
    def test_1(self, completion):
        assert completion
