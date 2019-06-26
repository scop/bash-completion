import pytest


class TestQuerybts:
    @pytest.mark.complete("querybts --", require_cmd=True)
    def test_1(self, completion):
        assert completion
