import pytest


@pytest.mark.bashcomp(cmd="apt-get")
class TestAptGet:
    @pytest.mark.complete("apt-get ")
    def test_1(self, completion):
        assert all(x in completion for x in "install update".split())

    @pytest.mark.complete("apt-get install ./", cwd="dpkg")
    def test_2(self, completion):
        assert completion == "bash-completion-test-subject.deb"

    @pytest.mark.complete("apt-get build-dep ")
    def test_build_dep_dirs(self, completion):
        assert "dpkg/" in completion
