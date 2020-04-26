import pytest


class TestBmake:
    @pytest.mark.complete("bmake -", require_cmd=True)
    def test_options(self, completion):
        assert completion
