import pytest

from conftest import assert_bash_exec


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

    @pytest.fixture(scope="class")
    def export_f_canary(self, request, bash):
        assert_bash_exec(bash, "_comp__test_export_f_canary() { return; }")

    @pytest.mark.complete("export -f _comp__test_export_f_canar")
    def test_no_equals_sign_for_function(self, completion, export_f_canary):
        assert completion
        assert "=" not in "".join(completion)
        assert completion.endswith(" ")
