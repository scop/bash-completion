import pytest


class TestCurlie:
    @pytest.mark.complete("curlie --", require_cmd=True)
    def test_options(self, completion):
        assert completion
