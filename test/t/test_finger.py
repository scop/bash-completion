import pytest

from conftest import assert_complete, partialize


class TestFinger:
    @pytest.fixture(scope="class")
    def users_at(self, bash, output_sort_uniq):
        return output_sort_uniq("compgen -u -S @")

    @pytest.mark.complete("finger ")
    def test_1(self, bash, completion, users_at):
        assert completion == users_at

    @pytest.mark.complete("finger r")
    def test_2(self, bash, completion, users_at):
        if not any(x.startswith("r") for x in users_at):
            pytest.skip("No users starting with r")
        assert completion
        idx = 1 if len(completion) == 1 else 0
        assert completion == sorted(
            x[idx:] for x in users_at if x.startswith("r")
        )
        assert not completion.endswith(" ")

    def test_partial_hostname(self, bash, known_hosts):
        first_char, partial_hosts = partialize(bash, known_hosts)
        user = "test"
        completion = assert_complete(bash, "finger %s@%s" % (user, first_char))
        if len(completion) == 1:
            assert completion == partial_hosts[0][1:]
        else:
            assert completion == ["%s@%s" % (user, x) for x in partial_hosts]
