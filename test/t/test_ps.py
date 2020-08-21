import pytest


class TestPs:
    @pytest.mark.complete("ps ")
    def test_1(self, completion):
        assert completion
