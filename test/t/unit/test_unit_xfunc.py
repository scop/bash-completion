import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None)
class TestUnitXfunc:
    def test_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR", "$PWD/_comp_xfunc", quote=False
            )

            # test precondition
            assert_bash_exec(
                bash,
                "! declare -F _comp_xfunc_xfunc_test1_utility1 &>/dev/null",
            )

            # first invocation (completion/xfunc-test1 is sourced)
            output = assert_bash_exec(
                bash,
                "_comp_xfunc xfunc-test1 utility1 'a b' cde fgh",
                want_output=True,
            )
            assert output.strip() == "util1[<a b><cde><fgh>]"

            # test precondition
            assert_bash_exec(
                bash, "declare -F _comp_xfunc_xfunc_test1_utility1 &>/dev/null"
            )

            # second invocation (completion/xfunc-test1 is not sourced)
            output = assert_bash_exec(
                bash,
                "_comp_xfunc xfunc-test1 utility1 'a b' cde fgh",
                want_output=True,
            )
            assert output.strip() == "util1[<a b><cde><fgh>]"

    def test_2(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR", "$PWD/_comp_xfunc", quote=False
            )

            # test precondition
            assert_bash_exec(
                bash, "! declare -F _comp_xfunc_non_standard_name &>/dev/null"
            )

            # first invocation (completion/xfunc-test2 is sourced)
            output = assert_bash_exec(
                bash,
                "_comp_xfunc xfunc-test2 _comp_xfunc_non_standard_name 'a b' cde fgh",
                want_output=True,
            )
            assert output.strip() == "util2[<a b><cde><fgh>]"

            # test precondition
            assert_bash_exec(
                bash, "declare -F _comp_xfunc_non_standard_name &>/dev/null"
            )

            # second invocation (completion/xfunc-test2 is not sourced)
            output = assert_bash_exec(
                bash,
                "_comp_xfunc xfunc-test2 _comp_xfunc_non_standard_name 'a b' cde fgh",
                want_output=True,
            )
            assert output.strip() == "util2[<a b><cde><fgh>]"
