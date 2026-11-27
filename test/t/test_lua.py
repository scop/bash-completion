import pytest

from conftest import assert_bash_exec, assert_complete


class TestLua:
    @pytest.mark.complete("lua ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lua -", require_cmd=True)
    def test_2(self, completion):
        assert completion


@pytest.mark.bashcomp(temp_cwd=True)
class TestLuaScript:
    @pytest.mark.parametrize(
        "arguments, expected",
        [
            ("scr", "ipt.lua"),
            ("-e 'x = 1' scr", "ipt.lua"),
            ("-ex=1 scr", "ipt.lua"),
            ("-l mod=sample scr", "ipt.lua"),
            ("-lmod=sample scr", "ipt.lua"),
            ("'-l' mod=sample scr", "ipt.lua"),
            ("-e scr", []),
            ('"-e" scr', []),
            ("-l scr", []),
            ("-- -scr", "ipt.lua"),
            ("'--' -scr", "ipt.lua"),
            ("script.lua samp", "le.txt"),
            ("-e 'x = 1' script.lua samp", "le.txt"),
            ("-l mod=sample script.lua samp", "le.txt"),
            ("-- -script.lua samp", "le.txt"),
            ("-- '-script.lua' samp", "le.txt"),
            ("- samp", "le.txt"),
            ("script.lua -samp", "le.txt"),
            ("script.lua -e samp", "le.txt"),
        ],
    )
    def test_filenames(self, bash, arguments, expected):
        assert_bash_exec(
            bash,
            "touch -- script.lua script.txt sample.txt "
            "-script.lua -script.txt -sample.txt",
        )
        assert assert_complete(bash, f"lua {arguments}") == expected

    @pytest.mark.parametrize("separator", [":", "="])
    @pytest.mark.parametrize(
        "script, extension", [("", "lua"), ("script.lua ", "txt")]
    )
    def test_filename_wordbreaks(self, bash, script, extension, separator):
        prefix = f"{extension}{separator}"
        assert_bash_exec(bash, f"touch '{prefix}config.{extension}'")
        completion = assert_complete(bash, f"lua {script}{prefix}con")
        assert completion == f"fig.{extension}"

    def test_escaped_space_before_wordbreak(self, bash):
        assert_bash_exec(bash, "touch 'spaced name=config.txt'")
        completion = assert_complete(bash, r"lua script.lua spaced\ name=con")
        assert completion == "fig.txt"
