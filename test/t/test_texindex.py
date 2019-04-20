import pytest


class TestTexindex:
    @pytest.mark.complete("texindex --")
    def test_1(self, completion):
        assert completion
