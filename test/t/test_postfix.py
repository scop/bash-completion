import pytest


class TestPostfix:

    @pytest.mark.complete("postfix ")
    def test_1(self, completion):
        assert completion.list
