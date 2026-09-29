import pytest


class TestE2label:
    @pytest.mark.complete("e2label ")
    def test_1(self, completion):
        assert completion
