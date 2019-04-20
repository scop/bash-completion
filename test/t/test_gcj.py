import pytest


class TestGcj:
    @pytest.mark.complete("gcj ")
    def test_1(self, completion):
        assert completion
