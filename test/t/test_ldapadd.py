import pytest


class TestLdapadd:
    @pytest.mark.complete("ldapadd -")
    def test_1(self, completion):
        assert completion
