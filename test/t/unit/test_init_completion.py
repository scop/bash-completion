import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitInitCompletion(object):

    def test_1(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash, 'foo() { local cur prev words cword; _init_completion; }; '
            'foo; unset foo')
