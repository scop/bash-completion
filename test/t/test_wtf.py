import pytest


class TestWtf:
    # TODO: actually requires an acronym db, not the cmd
    @pytest.mark.complete("wtf A", require_cmd=True)
    def test_1(self, completion):
        assert completion
