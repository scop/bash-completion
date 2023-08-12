import getpass

import pytest

from conftest import assert_complete


@pytest.mark.bashcomp(
    pre_cmds=(
        # Fake root command to get all users/groups completed at least for now
        "_comp_root_command=sudo",
    )
)
class TestChown:
    @pytest.mark.xfail(
        getpass.getuser() != "root", reason="Only root can chown to all users"
    )
    @pytest.mark.complete("chown ")
    def test_1(self, bash, completion, output_sort_uniq):
        users = output_sort_uniq("compgen -u")
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
        assert completion == full[len(part) :]
        assert completion.endswith(" ")

    def test_5(self, bash, part_full_user, part_full_group):
        _, user = part_full_user
        partgroup, fullgroup = part_full_group
        completion = assert_complete(bash, "chown %s:%s" % (user, partgroup))
        assert completion == fullgroup[len(partgroup) :]
        assert completion.output.endswith(" ")

    def test_6(self, bash, part_full_group):
        part, full = part_full_group
        completion = assert_complete(bash, "chown dot.user:%s" % part)
        assert completion == full[len(part) :]
        assert completion.output.endswith(" ")

    @pytest.mark.parametrize(
        "prefix",
        [
            r"funky\ user:",
            "funky.user:",
            r"funky\.user:",
            r"fu\ nky.user:",
            r"f\ o\ o\.\bar:",
            r"foo\_b\ a\.r\ :",
        ],
    )
    def test_7(self, bash, part_full_group, prefix):
        """Test preserving special chars in $prefix$partgroup<TAB>."""
        part, full = part_full_group
        completion = assert_complete(bash, "chown %s%s" % (prefix, part))
        assert completion == full[len(part) :]
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
