import pytest


@pytest.mark.bashcomp(cmd="dpkg-deb")
class TestDpkgDeb:
    @pytest.mark.complete("dpkg-deb --c")
    def test_1(self, completion):
        assert completion
