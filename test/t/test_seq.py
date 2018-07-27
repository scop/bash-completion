import pytest


class TestSeq:

    @pytest.mark.complete("seq --")
    def test_1(self, completion):
        assert completion.list
