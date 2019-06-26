import pytest


class TestUnshunt:
    @pytest.mark.complete("unshunt --", require_cmd=True)
    def test_1(self, completion):
        assert completion
