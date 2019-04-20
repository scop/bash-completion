import getpass

import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(
    pre_cmds=(
        # Fake root command to get all users/groups completed at least for now
        "root_command=sudo",
    )
)
class TestChown:
    @pytest.mark.xfail(
        getpass.getuser() != "root", reason="Only root can chown to all users"
    )
    @pytest.mark.complete("chown ")
    def test_1(self, bash, completion):
        users = sorted(
            assert_bash_exec(bash, "compgen -A user", want_output=True).split()
        )
        assert completion == users

    @pytest.mark.complete("chown foo: shared/default/")
    def test_2(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("chown :foo shared/default/")
    def test_3(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    def test_4(self, bash, part_full_user):
        part, full = part_full_user
        completion = assert_complete(bash, "chown %s" % part)
        assert completion == full
        assert completion.endswith(" ")

    def test_5(self, bash, part_full_user, part_full_group):
        _, user = part_full_user
        partgroup, fullgroup = part_full_group
        completion = assert_complete(bash, "chown %s:%s" % (user, partgroup))
        assert completion == "%s:%s" % (user, fullgroup)
        assert completion.output.endswith(" ")

    def test_6(self, bash, part_full_group):
        part, full = part_full_group
        completion = assert_complete(bash, "chown dot.user:%s" % part)
        assert completion == "dot.user:%s" % full
        assert completion.output.endswith(" ")

    @pytest.mark.xfail  # TODO check escaping, whitespace
    def test_7(self, bash, part_full_group):
        """Test preserving special chars in $prefix$partgroup<TAB>."""
        part, full = part_full_group
        for prefix in (
            r"funky\ user:",
            "funky.user:",
            r"funky\.user:",
            r"fu\ nky.user:",
            r"f\ o\ o\.\bar:",
            r"foo\_b\ a\.r\ :",
        ):
            completion = assert_complete(bash, "chown %s%s" % (prefix, part))
            assert completion == "%s%s" % (prefix, full)
            assert completion.output.endswith(" ")

    def test_8(self, bash, part_full_user, part_full_group):
        """Test giving up on degenerate cases instead of spewing junk."""
        _, user = part_full_user
        partgroup, _ = part_full_group
        for x in range(2, 5):
            completion = assert_complete(
                bash, "chown %s%s:%s" % (user, x * "\\", partgroup)
            )
            assert not completion

    def test_9(self, bash, part_full_group):
        """Test graceful fail on colon in user/group name."""
        part, _ = part_full_group
        completion = assert_complete(bash, "chown foo:bar:%s" % part)
        assert not completion
