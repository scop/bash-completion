import pytest


class TestYum:
    @pytest.mark.complete("yum -")
    def test_1(self, completion):
        assert completion
