import pytest


class TestOpera:

    @pytest.mark.complete("opera ")
    def test_1(self, completion):
        assert completion.list
