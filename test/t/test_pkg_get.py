import pytest


@pytest.mark.bashcomp(cmd="pkg-get")
class TestPkgGet:
    @pytest.mark.complete("pkg-get ")
    def test_1(self, completion):
        assert completion
