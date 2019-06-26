import pytest


class TestTexindex:
    @pytest.mark.complete("texindex --", require_cmd=True)
    def test_1(self, completion):
        assert completion
