import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitTilde(object):

    def test_1(self, bash):
        assert_bash_exec(bash, "_tilde >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            'foo() { local aa="~"; _tilde "$aa"; }; foo; unset foo')

    def test_3(self, bash):
        """Test for https://bugs.debian.org/766163"""
        assert_bash_exec(bash, '_tilde ~-o')
