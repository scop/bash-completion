import pytest


class TestPkgrm:
    @pytest.mark.complete("pkgrm ")
    def test_1(self, completion):
        assert completion
