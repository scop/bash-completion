import pytest


class TestPortsnap:
    @pytest.mark.complete("portsnap ")
    def test_1(self, completion):
        assert completion
