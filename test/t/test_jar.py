import pytest


class TestJar:
    @pytest.mark.complete("jar ")
    def test_1(self, completion):
        assert completion
