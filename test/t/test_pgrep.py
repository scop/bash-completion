import pytest


class TestPgrep:
    # "p": Assume that our process name completion runs ps
    @pytest.mark.complete("pgrep p")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pgrep -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete(
        "pgrep --nslist ",
        require_cmd=True,
        skipif=(
            "! pgrep --help 2>&1 | command grep -qF 'Available namespaces'"
        ),
    )
    def test_nslist(self, completion):
        assert completion
        assert not any("," in x for x in completion)

    @pytest.mark.complete(
        "pgrep --nslist foo,",
        require_cmd=True,
        skipif=(
            "! pgrep --help 2>&1 | command grep -qF 'Available namespaces'"
        ),
    )
    def test_nslist_after_comma(self, completion):
        assert completion
