import pytest


@pytest.mark.bashcomp(cmd="slapt-get")
class TestSlaptGet:
    @pytest.mark.complete("slapt-get -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("slapt-get --up")
    def test_2(self, completion):
        assert completion == "--update --upgrade".split()

    @pytest.mark.complete("slapt-get -c non-existent-file --install ")
    def test_3(self, completion):
        assert not completion
