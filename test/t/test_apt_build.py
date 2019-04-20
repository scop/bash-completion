import pytest


@pytest.mark.bashcomp(cmd="apt-build")
class TestAptBuild:
    @pytest.mark.complete("apt-build ")
    def test_1(self, completion):
        assert completion
