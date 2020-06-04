import pytest

from conftest import assert_bash_exec


class TestGcc:
    @pytest.fixture(scope="class")
    def gcc_with_completion(self, bash):
        got = assert_bash_exec(
            bash, "gcc --help=common || :", want_output=True
        )
        if "--completion" not in got:
            pytest.skip("GCC does not support --completion")

    @pytest.fixture(scope="class")
    def gcc_x86(self, bash):
        got = assert_bash_exec(bash, "gcc -v || :", want_output=True)
        if "Target: x86" not in got:
            pytest.skip("Not a x86 GCC")

    @pytest.mark.complete("gcc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gcc -fsanitize=add")
    def test_enum_value(self, completion, gcc_with_completion):
        assert completion == "ress"

    @pytest.mark.complete("gcc -fsanitize=")
    def test_enum_value_with_eq(self, completion, gcc_with_completion):
        assert "address" in completion

    @pytest.mark.complete("gcc -fno-ipa-ic")
    def test_negative_option(self, completion, gcc_with_completion):
        assert "-fno-ipa-icf" in completion

    @pytest.mark.complete("gcc -fxyz-abc")
    def test_no_completion(self, completion):
        assert not completion

    @pytest.mark.complete("gcc --param ")
    def test_param_with_space(self, completion, gcc_with_completion):
        assert len(completion) > 50
        # starting with GCC 10.1 param end with =
        assert (
            "lto-partitions" in completion or "lto-partitions=" in completion
        )

    @pytest.mark.complete("gcc --param=lto-max-p")
    def test_param_with_eq(self, completion, gcc_with_completion):
        # starting with GCC 10.1 param ends with =
        assert completion in ("artition", "artition=")

    @pytest.mark.complete("gcc -march=amd")
    def test_march(self, completion, gcc_with_completion, gcc_x86):
        assert completion == "fam10"

    @pytest.mark.complete("gcc -march=")
    def test_march_native(self, completion, gcc_with_completion):
        assert "native" in completion

    @pytest.mark.complete("gcc -mtune=")
    def test_mtune_generic(self, completion, gcc_with_completion):
        assert "generic" in completion
