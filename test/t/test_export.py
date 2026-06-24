import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


class TestExport:
    @pytest.mark.complete("export BASH")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("export -n BASH")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("export -p ")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("export FOO=", cwd="shared/default")
    def test_4(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("export FOO=f", cwd="shared/default")
    def test_5(self, completion):
        assert completion == ["foo", "foo.d/"]

    @pytest.mark.complete("export -fn _comp_cmd_ex")
    def test_6(self, completion):
        assert completion == "port"

    @pytest.mark.complete(r"export FOO=$BASH")
    def test_7(self, completion):
        assert completion

    @pytest.mark.complete("export -", require_cmd=True)
    def test_8(self, completion):
        assert completion

    @pytest.mark.complete("export BASH_VERSIO")
    def test_no_equals_sign_for_variable_incomplete(self, completion):
        """When the variable name is completed, we should not
        immediately suffix the equal sign.  The equal sign will be
        appended on a further TAB after the word becomes a complete
        variable name.
        """
        assert completion
        assert "=" not in "".join(completion)
        assert not completion.endswith(" ")

    @pytest.mark.complete("export BASH")
    def test_no_equals_sign_for_variable_ambiguous(self, completion):
        """When the completion is not unique, we should not suffix the
        equal sign.
        """
        assert completion
        assert "=" not in "".join(completion)
        assert not completion.endswith(" ")

    @pytest.mark.complete("export BASH_VERSION")
    def test_no_equals_sign_for_variable_complete(self, completion):
        """Only when the current word is already complete and matches
        unique completion, we should suffix the equal sign.
        """
        assert completion
        assert "=" in "".join(completion)

    @pytest.fixture(scope="class")
    def export_f_canary(self, request, bash):
        assert_bash_exec(bash, "_comp__test_export_f_canary() { return; }")

    @pytest.mark.complete("export -f _comp__test_export_f_canar")
    def test_no_equals_sign_for_function_incomplete(
        self, completion, export_f_canary
    ):
        assert completion
        assert "=" not in "".join(completion)
        assert completion.endswith(" ")

    @pytest.mark.complete("export -f _comp__test_export_f_canary")
    def test_no_equals_sign_for_function_complete(
        self, completion, export_f_canary
    ):
        """We can suffix a space to a function name because there is
        no possibility that the equal sign is suffixed to a function
        name."""
        assert completion.output == " "

    @pytest.mark.complete("export -f -")
    def test_second_option(self, completion):
        assert completion

    def test_custom_IFS(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("IFS", "i")
            completion = assert_complete(bash, "export BASH")
            assert completion
