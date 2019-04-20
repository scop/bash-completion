import pytest


@pytest.mark.bashcomp(cmd="dpkg-source")
class TestDpkgSource:
    @pytest.mark.complete("dpkg-source -")
    def test_1(self, completion):
        assert completion
