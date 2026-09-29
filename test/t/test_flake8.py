import pytest


class TestFlake8:
    @pytest.mark.complete("flake8 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "flake8 -", require_cmd=True, xfail="! flake8 --help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("flake8 --doesnt-exist=")
    def test_3(self, completion):
        assert not completion
