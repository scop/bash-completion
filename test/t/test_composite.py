import pytest


class TestComposite:
    @pytest.mark.complete("composite ")
    def test_1(self, completion):
        assert completion
