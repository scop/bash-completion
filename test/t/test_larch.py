import pytest


class TestLarch:
    @pytest.mark.complete("larch library-")
    def test_1(self, completion):
        assert completion
