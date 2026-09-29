import pytest


class TestPkgDelete:
    @pytest.mark.complete("pkg_delete ")
    def test_1(self, completion):
        assert completion
