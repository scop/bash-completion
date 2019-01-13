import pytest


class TestAclocal:

    @pytest.mark.complete("aclocal ")
    def test_1(self, completion):
        assert completion
