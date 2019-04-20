import pytest

from conftest import assert_bash_exec


class TestCpio:
    @pytest.mark.complete("cpio --")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cpio -R ")
    def test_2(self, bash, completion):
        users = sorted(
            assert_bash_exec(bash, "compgen -A user", want_output=True).split()
        )
        assert completion == users
