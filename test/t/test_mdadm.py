import pytest


class TestMdadm:
    @pytest.mark.complete("mdadm ")
    def test_1(self, completion):
        assert completion
