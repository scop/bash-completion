import pytest

from conftest import in_docker


class TestArp:

    @pytest.mark.xfail(in_docker(), reason="Probably fails in docker")
    @pytest.mark.complete("arp ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("arp -")
    def test_2(self, completion):
        assert completion
