import pytest


class TestGrpck:
    @pytest.mark.complete("grpck ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("grpck -", require_cmd=True)
    def test_2(self, completion):
        assert completion
