# Based on work by Stephen Gildea, October 2010.

import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+declare -f fn$")
class TestUnitParseHelp:
    def test_1(self, bash):
        assert_bash_exec(bash, "fn() { echo; }")
        output = assert_bash_exec(bash, "_parse_help fn; (($? == 1))")
        assert not output

    def test_2(self, bash):
        assert_bash_exec(bash, "fn() { echo 'no dashes here'; }")
        output = assert_bash_exec(bash, "_parse_help fn; (($? == 1))")
        assert not output

    def test_3(self, bash):
        assert_bash_exec(bash, "fn() { echo 'internal-dash'; }")
        output = assert_bash_exec(bash, "_parse_help fn; (($? == 1))")
        assert not output

    def test_4(self, bash):
        assert_bash_exec(bash, "fn() { echo 'no -leading-dashes'; }")
        output = assert_bash_exec(bash, "_parse_help fn; (($? == 1))")
        assert not output

    def test_5(self, bash):
        assert_bash_exec(bash, "fn() { echo '-one dash'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "-one".split()

    def test_6(self, bash):
        assert_bash_exec(bash, "fn() { echo ' -space dash'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "-space".split()

    def test_7(self, bash):
        assert_bash_exec(bash, "fn() { echo '-one -two dashes'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "-one".split()

    def test_8(self, bash):
        assert_bash_exec(bash, "fn() { echo '-one,-t dashes'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "-one".split()

    def test_9(self, bash):
        assert_bash_exec(bash, "fn() { echo '-one dash-inside'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "-one".split()

    def test_10(self, bash):
        """Test value not included in completion."""
        assert_bash_exec(bash, "fn() { echo '--long-arg=value'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--long-arg=".split()

    def test_11(self, bash):
        """Test -value not seen as option."""
        assert_bash_exec(bash, "fn() { echo '--long-arg=-value'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--long-arg=".split()

    def test_12(self, bash):
        assert_bash_exec(bash, "fn() { echo '--long-arg=-value,--opt2=val'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--long-arg=".split()

    def test_13(self, bash):
        assert_bash_exec(bash, "fn() { echo '-m,--mirror'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--mirror".split()

    def test_14(self, bash):
        assert_bash_exec(bash, "fn() { echo '-T/--upload-file'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--upload-file".split()

    def test_15(self, bash):
        assert_bash_exec(bash, "fn() { echo '-T|--upload-file'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--upload-file".split()

    def test_16(self, bash):
        assert_bash_exec(bash, "fn() { echo '-f, -F, --foo'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_17(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo[=bar]'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_17_failglob(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo[=bar]'; }")
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_17_nullglob(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo[=bar]'; }")
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", True)
            output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_18(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo=<bar>'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo=".split()

    def test_19(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo={bar,quux}'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo=".split()

    def test_20(self, bash):
        assert_bash_exec(bash, "fn() { echo '--[no]foo'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo --nofoo".split()

    def test_21(self, bash):
        assert_bash_exec(bash, "fn() { echo '--[no-]bar[=quux]'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--bar --no-bar".split()

    def test_22(self, bash):
        assert_bash_exec(bash, "fn() { echo '--[no-]bar=quux'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--bar= --no-bar=".split()

    def test_23(self, bash):
        assert_bash_exec(bash, "fn() { echo '--[dont-]foo'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo --dont-foo".split()

    def test_24(self, bash):
        assert_bash_exec(bash, "fn() { echo '-[dont]x --[dont]yy'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--yy --dontyy".split()

    def test_25(self, bash):
        assert_bash_exec(bash, "fn() { echo '-f FOO, --foo=FOO'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo=".split()

    def test_26(self, bash):
        assert_bash_exec(bash, "fn() { echo '-f [FOO], --foo[=FOO]'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_27(self, bash):
        assert_bash_exec(bash, "fn() { echo '--foo.'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_27_middle_dot(self, bash):
        """We do not want to include the period at the end of the sentence but
        want to include dots connecting names."""
        assert_bash_exec(bash, "fn() { echo '--foo.bar.'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo.bar".split()

    def test_28(self, bash):
        assert_bash_exec(bash, "fn() { echo '-f or --foo'; }")
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--foo".split()

    def test_29(self, bash):
        """Test parsing from stdin."""
        output = assert_bash_exec(
            bash, "echo '-f or --foo' | _parse_help -", want_output=True
        )
        assert output.split() == "--foo".split()

    def test_30(self, bash):
        """More than two dashes should not be treated as options."""
        assert_bash_exec(
            bash, r"fn() { printf '%s\n' $'----\n---foo\n----- bar'; }"
        )
        output = assert_bash_exec(bash, "_parse_help fn; (($? == 1))")
        assert not output

    def test_31(self, bash):
        assert_bash_exec(
            bash,
            r"fn() { printf '%s\n' "
            r"'-F ERROR_FORMAT, --error-format ERROR_FORMAT'; }",
        )
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--error-format".split()

    def test_32(self, bash):
        assert_bash_exec(
            bash,
            r"fn() { printf '%s\n' "
            r"'-e CODE1,CODE2..  --exclude=CODE1,CODE2..'; }",
        )
        output = assert_bash_exec(bash, "_parse_help fn", want_output=True)
        assert output.split() == "--exclude=".split()

    def test_custom_helpopt1(self, bash):
        assert_bash_exec(bash, "fn() { [[ $1 == -h ]] && echo '-option'; }")
        output = assert_bash_exec(bash, "_parse_help fn -h", want_output=True)
        assert output.split() == "-option".split()

    def test_custom_helpopt2(self, bash):
        assert_bash_exec(bash, "fn() { [[ $1 == '-?' ]] && echo '-option'; }")
        output = assert_bash_exec(
            bash, "_parse_help fn '-?'", want_output=True
        )
        assert output.split() == "-option".split()

    def test_custom_helpopt2_failglob(self, bash):
        assert_bash_exec(bash, "fn() { [[ $1 == '-?' ]] && echo '-option'; }")
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash, "_parse_help fn '-?'", want_output=True
            )
        assert output.split() == "-option".split()

    def test_custom_helpopt2_nullglob(self, bash):
        assert_bash_exec(bash, "fn() { [[ $1 == '-?' ]] && echo '-option'; }")
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", True)
            output = assert_bash_exec(
                bash, "_parse_help fn '-?'", want_output=True
            )
        assert output.split() == "-option".split()
