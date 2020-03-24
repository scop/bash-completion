import pytest


@pytest.mark.bashcomp(cmd="apt-mark")
class TestAptMark:
    @pytest.mark.complete("apt-mark ")
    def test_1(self, completion):
        assert all(x in completion for x in (
        "auto manual remove showinstall showremove "
        "hold minimize-manual showauto showmanual unhold install "
        "purge showhold showpurge").split())

    @pytest.mark.complete("apt-mark minimize-manual ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("apt-mark --file=", cwd="dpkg")
    def test_3(self, completion):
        assert completion == "--file=bash-completion-test-subject.deb"

    @pytest.mark.complete("apt-mark --config-file ", cwd="dpkg")
    def test_4(self, completion):
        assert completion == "bash-completion-test-subject.deb"

    @pytest.mark.complete("apt-mark --option ")
    def test_5(self, completion):
        assert not completion

