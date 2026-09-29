import pytest


class TestPyston:
    @pytest.mark.complete("pyston ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("pyston -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete(
        "pyston -b",
        require_cmd=True,
        skipif="! pyston -h | command grep -qwF -- -bb",
    )
    def test_bb(self, completion):
        assert "-bb" in completion
