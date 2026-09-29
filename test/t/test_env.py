import pytest

from conftest import assert_complete


class TestEnv:
    @pytest.mark.complete("env --", require_longopt=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("env __unknown_variable__=")
    def test_unknown_variable_falls_back_to_filedir(self, completion):
        assert "shared/" in completion

    @pytest.mark.complete("env LANG=", xfail="! locale -a &>/dev/null")
    def test_lang_envvar(self, completion):
        assert any(x == "C" or x.startswith("C.") for x in completion)

    @pytest.mark.parametrize(
        "opts",
        [
            "",
            "foo=bar",
            "--debug",
            "--debug foo=bar",
            "-",
            "- foo=bar",
        ],
    )
    def test_command(self, bash, opts):
        completion = assert_complete(bash, "env %s s" % opts)
        assert completion == "h" or "sh" in completion

    @pytest.mark.parametrize(
        "opts",
        [
            "foo=bar --non-existent",
            "- --non-existent",
            "-- --non-existent",
        ],
    )
    def test_option_like_command(self, bash, opts):
        completion = assert_complete(bash, "env %s s" % opts)
        assert not (completion == "h" or "sh" in completion)
