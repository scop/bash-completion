import pytest

from conftest import in_docker


class TestIfdown:

    @pytest.mark.xfail(in_docker(), reason="Probably fails in docker")
    @pytest.mark.complete("ifdown ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ifdown bash-completion ")
    def test_2(self, completion):
        assert not completion
