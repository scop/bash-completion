import pytest


class TestDmypy:
    @pytest.mark.complete(
        "dmypy ", require_cmd=True, xfail="! dmypy --help &>/dev/null"
    )
    def test_commands(self, completion):
        assert "help" in completion
        assert not any("," in x for x in completion)

    @pytest.mark.complete("dmypy -", require_cmd=True, require_longopt=True)
    def test_options(self, completion):
        assert "--help" in completion
