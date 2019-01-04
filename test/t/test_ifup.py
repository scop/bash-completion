import pytest

from conftest import in_docker


class TestIfup:

    @pytest.mark.xfail(in_docker(), reason="Probably fails in docker")
    @pytest.mark.complete("ifup ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ifup --", skipif="! ifup --help &>/dev/null")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("ifup bash-completion ")
    def test_3(self, completion):
        assert not completion.list
