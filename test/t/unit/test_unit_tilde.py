import pytest

from conftest import assert_bash_exec, find_unique_completion_pair


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitTilde:

    @pytest.fixture
    def part_full(self, bash):
        res = assert_bash_exec(
            bash, "compgen -u", want_output=True,
        ).strip().split()
        pair = find_unique_completion_pair(res)
        if not pair:
            pytest.skip("No suitable test user found")
        return pair

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

    def _test_part_full(self, bash, part, full):
        res = assert_bash_exec(
            bash,
            '_tilde "~%s"; echo "${COMPREPLY[@]}"' % part,
            want_output=True,
        ).strip().split()
        assert res
        assert res[0] == "~%s" % full

    def test_4(self, bash, part_full):
        """~full should complete to ~full unmodified."""
        _, full = part_full
        self._test_part_full(bash, full, full)

    def test_5(self, bash, part_full):
        """~part should complete to ~full."""
        part, full = part_full
        self._test_part_full(bash, part, full)
