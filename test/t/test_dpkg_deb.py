import pytest


@pytest.mark.bashcomp(cmd="dpkg-deb")
class TestDpkgDeb:
    @pytest.mark.complete("dpkg-deb --c", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dpkg-deb --show b", cwd="dpkg")
    def test_show(self, completion):
        assert completion == "ash-completion-test-subject.deb"
