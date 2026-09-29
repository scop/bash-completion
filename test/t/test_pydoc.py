import pytest


class TestPydoc:
    @pytest.mark.complete("pydoc r", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pydoc -", require_cmd=True)
    def test_2(self, completion):
        assert completion
