import pytest


class TestBison:
    @pytest.mark.complete("bison --", require_cmd=True)
    def test_1(self, completion):
        assert completion
