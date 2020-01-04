import pytest

from conftest import assert_bash_exec, assert_complete, partialize


class TestFinger:
    @pytest.fixture(scope="class")
    def users_at(self, bash):
        return sorted(
            assert_bash_exec(
                bash, "compgen -A user -S @", want_output=True
            ).split()
        )

    @pytest.mark.complete("finger ")
    def test_1(self, bash, completion, users_at):
        assert completion == users_at

    @pytest.mark.complete("finger r")
    def test_2(self, bash, completion, users_at):
        if not any(x.startswith("r") for x in users_at):
            pytest.skip("No users starting with r")
        assert completion
        assert all(x.startswith("r") for x in completion)
        assert not completion.endswith(" ")

    def test_partial_hostname(self, bash, known_hosts):
        first_char, partial_hosts = partialize(bash, known_hosts)
        user = "test"
        completion = assert_complete(bash, "finger %s@%s" % (user, first_char))
        assert completion == ["%s@%s" % (user, x) for x in partial_hosts]
