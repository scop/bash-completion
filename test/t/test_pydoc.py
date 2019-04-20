import pytest


class TestPydoc:
    @pytest.mark.complete("pydoc r")
    def test_1(self, completion):
        assert completion
