import pytest


class TestAbook:
    @pytest.mark.complete("abook -", require_cmd=True)
    def test_1(self, completion):
        assert completion
