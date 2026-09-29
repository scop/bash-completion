import pytest


class TestCardctl:
    @pytest.mark.complete("cardctl ")
    def test_1(self, completion):
        assert completion
