import pytest


@pytest.mark.bashcomp(cmd="dpkg-reconfigure")
class TestDpkgReconfigure:
    @pytest.mark.complete("dpkg-reconfigure --")
    def test_1(self, completion):
        assert completion
