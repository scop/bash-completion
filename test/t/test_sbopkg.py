import pytest


class TestSbopkg:
    @pytest.mark.complete("sbopkg -")
    def test_1(self, completion):
        assert completion
