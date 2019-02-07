import pytest


class TestIfstat:

    @pytest.mark.complete("ifstat -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ifstat -i ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ifstat -d ")
    def test_3(self, completion):
        assert completion
