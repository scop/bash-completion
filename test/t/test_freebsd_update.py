import pytest


@pytest.mark.bashcomp(cmd="freebsd-update")
class TestFreebsdUpdate:
    @pytest.mark.complete("freebsd-update ")
    def test_1(self, completion):
        assert completion
