import pytest


class TestHelp:
    @pytest.mark.complete("help ")
    def test_basic(self, completion):
        assert "help" in completion

    @pytest.mark.complete("help -")
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete(
        r"help \(",
        skipif="! compgen -A helptopic | grep -qxF '(( ... ))'",  # bash 4.2
    )
    def test_parens(self, completion):
        # Assumption: an item like "(( ... ))" exists in the output
        assert any(
            x.startswith(r"\(") and x.endswith(r"\)\)") for x in completion
        )
