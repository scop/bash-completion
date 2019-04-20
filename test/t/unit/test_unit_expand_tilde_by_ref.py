import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitExpandTildeByRef:
    def test_1(self, bash):
        assert_bash_exec(bash, "__expand_tilde_by_ref >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            '_x() { local aa="~"; __expand_tilde_by_ref aa; }; _x; unset _x',
        )
