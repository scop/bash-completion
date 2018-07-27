import pytest


class TestGetent:

    @pytest.mark.complete("getent ")
    def test_1(self, completion):
        assert completion.list
