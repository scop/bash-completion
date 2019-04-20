import pytest


class TestGcl:
    @pytest.mark.complete("gcl ")
    def test_1(self, completion):
        assert completion
