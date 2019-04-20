import pytest


class TestA2ps:
    @pytest.mark.complete("a2ps ")
    def test_1(self, completion):
        assert completion
