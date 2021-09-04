import pytest

from conftest import TestUnitBase, assert_bash_exec, assert_complete


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMP(_(WORDS|CWORD|LINE|POINT)|REPLY)|cur|cword|words)=",
)
class TestUnitCommandOffset:
    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            "_co1() { _command_offset 1; }; "
            "complete -F _co1 co1",
        )

    def test_1(self, bash, functions):
        assert_complete(bash, 'co1 "/tmp/aaa bbb" ')
        assert_bash_exec(bash, "! complete -p aaa", want_output=None)

