import pytest


class TestVgreduce:
    @pytest.mark.complete("vgreduce -", skipif="! vgreduce --help &>/dev/null")
    def test_1(self, completion):
        assert completion
