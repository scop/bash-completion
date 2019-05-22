import pytest


class TestIfstat:
    @pytest.mark.complete("ifstat -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "ifstat -i ", xfail="ifstat -v | command grep -qF iproute2"
    )
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete(
        "ifstat -d ", xfail="ifstat -v | command grep -qF iproute2"
    )
    def test_3(self, completion):
        assert completion
