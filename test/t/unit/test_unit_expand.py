import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitExpand:
    def test_1(self, bash):
        assert_bash_exec(bash, "_expand >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(bash, "foo() { _expand; }; foo; unset foo")
