import pytest


class Test(object):

    @pytest.mark.complete("apt-get ")
    def test_(self, completion):
        assert "install" in completion.list and "update" in completion.list

    @pytest.mark.complete("apt-get install ./", cwd="dpkg")
    def test_local_install(self, completion):
        assert completion.list == ["./bash-completion-test-subject.deb"]
