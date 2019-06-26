import pytest


class TestSbopkg:
    @pytest.mark.complete("sbopkg -", require_cmd=True)
    def test_1(self, completion):
        assert completion
