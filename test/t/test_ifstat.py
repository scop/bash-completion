import pytest


class TestIfstat:

    @pytest.mark.complete("ifstat -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ifstat -i ",
                          skipif="ifstat -v | command grep -qF iproute2")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ifstat -d ",
                          skipif="ifstat -v | command grep -qF iproute2")
    def test_3(self, completion):
        assert completion
