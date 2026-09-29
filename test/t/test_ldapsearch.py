import pytest


class TestLdapsearch:
    @pytest.mark.complete("ldapsearch -")
    def test_1(self, completion):
        assert completion
