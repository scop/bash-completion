import pytest


class TestUnshunt:
    @pytest.mark.complete("unshunt --")
    def test_1(self, completion):
        assert completion
