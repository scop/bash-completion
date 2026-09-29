import pytest


class TestGroupmems:
    @pytest.mark.complete("groupmems -", require_cmd=True)
    def test_1(self, completion):
        assert completion
