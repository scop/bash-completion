import pytest


@pytest.mark.bashcomp(
    cmd="apt-get",
)
class TestAptGet:

    @pytest.mark.complete("apt-get ")
    def test_1(self, completion):
        assert "install" in completion.list and "update" in completion.list

    @pytest.mark.complete("apt-get install ./", cwd="dpkg")
    def test_2(self, completion):
        assert completion.list == ["./bash-completion-test-subject.deb"]
