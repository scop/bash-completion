import pytest

from conftest import in_container


class TestIfdown:
    @pytest.mark.xfail(in_container(), reason="Probably fails in a container")
    @pytest.mark.complete("ifdown ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ifdown bash-completion ")
    def test_2(self, completion):
        assert not completion
