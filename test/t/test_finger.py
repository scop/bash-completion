import pytest

from conftest import assert_bash_exec


class TestFinger:

    @pytest.mark.complete("finger ")
    def test_1(self, bash, completion):
        users_at = sorted(assert_bash_exec(
            bash, "compgen -A user -S @", want_output=True).split())
        assert completion.list == users_at
