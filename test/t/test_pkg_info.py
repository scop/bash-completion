import pytest


class TestPkgInfo:
    @pytest.mark.complete("pkg_info ")
    def test_1(self, completion):
        assert completion
