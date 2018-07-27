import pytest


class TestGrpck:

    @pytest.mark.complete("grpck ")
    def test_1(self, completion):
        assert completion.list
