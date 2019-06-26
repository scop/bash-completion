import pytest


@pytest.mark.bashcomp(cmd="pkg-config")
class TestPkgConfig:
    @pytest.mark.complete("pkg-config ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pkg-config -", require_cmd=True)
    def test_2(self, completion):
        assert completion
