import pytest


@pytest.mark.bashcomp(cmd="apt-mark")
class TestAptMark:
    @pytest.mark.complete("apt-mark ")
    def test_1(self, completion):
        assert all(
            x in completion
            for x in (
                "auto manual remove showinstall showremove "
                "hold minimize-manual showauto showmanual unhold install "
                "purge showhold showpurge"
            ).split()
        )

    @pytest.mark.complete("apt-mark minimize-manual ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("apt-mark --file=", cwd="dpkg")
    def test_3(self, completion):
        assert (
            completion
            == "bash-completion-test-nonsubject.txt bash-completion-test-subject.deb".split()
        )

    @pytest.mark.complete("apt-mark --config-file ", cwd="apt-mark")
    def test_4(self, completion):
        assert completion == "example.conf"

    @pytest.mark.complete("apt-mark --option ")
    def test_5(self, completion):
        assert not completion

    @pytest.mark.complete("apt-mark --dont-fail-in-unset-mode")
    def test_unknown_option(self, completion):
        # Just see that it does not error out
        pass
