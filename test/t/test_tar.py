import re

import pytest

from conftest import PS1, assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(ignore_env=r"^-declare -f _comp_cmd_tar$")
class TestTar:
    @pytest.fixture(scope="class")
    def gnu_tar(self, bash):
        got = assert_bash_exec(bash, "tar --version || :", want_output=True)
        if not re.search(r"\bGNU ", got):
            pytest.skip("Not GNU tar")

    @pytest.mark.complete("tar ", shopt=dict(failglob=True))
    def test_1(self, bash, completion):
        assert completion

    # Test "f" when mode is not as first option
    @pytest.mark.complete("tar zfc ", cwd="tar")
    def test_2(self, completion):
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar cf ", cwd="tar")
    def test_3(self, completion):
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar tf archive.tar.xz dir/file", cwd="tar")
    def test_4(self, completion):
        assert completion == "dir/fileA dir/fileB dir/fileC".split()

    @pytest.mark.complete("tar cTfvv NOT_EXISTS DONT_CREATE.tar ", cwd="tar")
    def test_5(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/ escape.tar".split()

    @pytest.mark.complete("tar xvf ", cwd="tar")
    def test_6(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/ escape.tar".split()

    @pytest.mark.complete("tar -c")
    def test_7(self, completion, gnu_tar):
        """Test short options."""
        assert completion

    @pytest.mark.complete("tar -zcf ", cwd="tar")
    def test_8(self, completion, gnu_tar):
        """Test mode not as first option."""
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar -cf ", cwd="tar")
    def test_9(self, completion, gnu_tar):
        """Test that we don't suggest rewriting existing archive."""
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar -c --file ", cwd="tar")
    def test_10(self, completion, gnu_tar):
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar -cvv --file ", cwd="tar")
    def test_11(self, completion, gnu_tar):
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete("tar -tf archive.tar.xz dir/file", cwd="tar")
    def test_12(self, completion, gnu_tar):
        """Test archive listing."""
        assert completion == "dir/fileA dir/fileB dir/fileC".split()

    @pytest.mark.complete("tar -t --file archive.tar.xz dir/file", cwd="tar")
    def test_13(self, completion, gnu_tar):
        """Test archive listing with --file."""
        assert completion == "dir/fileA dir/fileB dir/fileC".split()

    @pytest.mark.complete("tar --block")
    def test_14(self, completion, gnu_tar):
        assert completion == "--block-number --blocking-factor=".split()

    @pytest.mark.complete("tar --add-fil")
    def test_15(self, completion, gnu_tar):
        assert completion == "e="
        assert not completion.endswith(" ")

    @pytest.mark.complete("tar -cf /dev/null --posi")
    def test_16(self, completion, gnu_tar):
        assert completion == "x"
        assert completion.endswith(" ")

    @pytest.mark.complete("tar --owner=")
    def test_17(self, bash, completion, gnu_tar, output_sort_uniq):
        users = output_sort_uniq("compgen -u")
        assert completion == users

    @pytest.mark.complete("tar --group=")
    def test_18(self, bash, completion, gnu_tar, output_sort_uniq):
        groups = output_sort_uniq("compgen -g")
        assert completion == groups

    # Use -b for this as -b is still not handled by tar's completion
    @pytest.mark.complete("tar -cvvfb ")
    def test_19(self, bash, completion, gnu_tar):
        """Test short option -XXXb <TAB> (arg required)."""
        assert not completion

    # Use bsdtar here as it completes to only 'zc zt zx'
    # -- 'tar' can be GNU tar and have more options
    @pytest.mark.complete("bsdtar z")
    def test_20(self, bash, completion):
        assert completion == "zc zt zx".split()

    @pytest.mark.complete("bsdtar cbfvv NON_EXISTENT ", cwd="tar")
    def test_21(self, bash, completion):
        """Test _second_ option in "old" argument."""
        assert completion == "dir/ dir2/".split()

    @pytest.mark.complete(r"tar tf escape.tar a/b\'", cwd="tar")
    def test_22(self, bash, completion):
        """Test listing escaped chars in old option."""
        assert completion == "c/"

    # Test long options (gnu style)
    @pytest.mark.complete("tar --create --file created.tar ", cwd="tar")
    def test_23(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/ escape.tar".split()

    # Test detection of file type by extension, J is for .xz
    @pytest.mark.complete("tar xJf ", cwd="tar")
    def test_24(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/".split()

    # Test compression detection of gnu style options
    @pytest.mark.complete("tar --extract --xz --file ", cwd="tar")
    def test_25(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/".split()

    # TODO: "tar tf escape.tar a/b"


@pytest.mark.bashcomp(cmd="bsdtar")
class TestBsdtarCombinedOptions:
    @pytest.mark.parametrize(
        "command",
        [
            "bsdtar -tf ",
            "bsdtar -C . -tvf ",
            "bsdtar -C. -tf ",
            "bsdtar -C -c -tf ",
            "bsdtar -C-c -tf ",
            "bsdtar --list -vf ",
            "bsdtar --exclude=pattern -tf ",
            "bsdtar --exclude -c -tf ",
            "bsdtar -W exclude -c -tf ",
        ],
    )
    def test_archive_argument(self, bash, command):
        assert assert_complete(bash, command, cwd="bsdtar") == [
            "test.pax",
            "test.rar",
        ]

    @pytest.mark.parametrize(
        "command", ["bsdtar -C -t -cf ", "bsdtar -C-t -cf "]
    )
    def test_create_archive_argument(self, bash, command):
        assert assert_complete(bash, command, cwd="tar") == ["dir/", "dir2/"]

    @pytest.mark.complete("bsdtar -C-c -vf test.", trail=" -t", cwd="bsdtar")
    def test_mode_after_archive_argument(self, completion):
        assert completion == ["test.pax", "test.rar"]

    @pytest.mark.parametrize(
        "command,trail",
        [
            ("bsdtar -vf test.", " -C -c -t"),
            ("bsdtar -vf test.", " -C-c -t"),
            ("bsdtar -vf test.", " -C -- -t"),
            ("bsdtar --list -vf test.", " -- -c"),
            ("bsdtar -C-t -vf test.", " -C -c -t"),
        ],
    )
    def test_mode_with_arguments_after_cursor(self, bash, command, trail):
        assert assert_complete(bash, command, trail=trail, cwd="bsdtar") == [
            "test.pax",
            "test.rar",
        ]

    @pytest.mark.parametrize(
        "trail,archive",
        [
            (" --exclude pattern -t", "test.rar"),
            (" --exclude=pattern -t", "test.rar"),
            (" --exclude -c -t", "test.rar"),
            (" --directory -c -t", "test.rar"),
            (" --exclude-fr patterns -t", "test.rar"),
            (" --no-recursion -t", "test.rar"),
            (" --lis", "test.rar"),
            (" -W exclude pattern -t", "test.rar"),
            (" -W exclude=pattern -t", "test.rar"),
            (" -Wexclude pattern -t", "test.rar"),
            (" -Wexclude=pattern -t", "test.rar"),
            (" -W exclude -c -t", "test.rar"),
            (" -tW exclude pattern", "test.rar"),
            (" -tWexclude=pattern", "test.rar"),
            (" -Wlist", "test.rar"),
            (" -CW -t", "test.rar"),
            (" --excl -t", "test.shar"),
            (" -Wexcl -t", "test.shar"),
            (" --unknown-option -t", "test.shar"),
            (" --no-recursion=1 -t", "test.shar"),
        ],
    )
    def test_long_options_after_archive_argument(self, bash, trail, archive):
        with bash_env_saved(bash, sendintr=True) as bash_env:
            bash_env.chdir("bsdtar")
            bash.send("bsdtar -vf test." + trail + "\002" * len(trail) + "\t")
            bash.expect(
                r"\r\n((?:test\.[a-z]+\r\n)+)" + re.escape(PS1), timeout=5
            )
            assert bash.match.group(1).splitlines() == ["test.pax", archive]

    @pytest.mark.complete("bsdtar -vf escape.", trail=" --xz -t", cwd="tar")
    def test_compression_option_after_archive_argument(self, completion):
        assert not completion

    @pytest.mark.complete("bsdtar -cb ", cwd="tar")
    def test_block_size_argument(self, completion):
        assert not completion

    @pytest.mark.parametrize(
        "command",
        [
            "bsdtar -tfarchivef ",
            "bsdtar -tbf ",
            "bsdtar -tCf ",
            "bsdtar -t -f -tf ",
            "bsdtar -t -- -tf ",
            "bsdtar -t --exclude -tf ",
        ],
    )
    def test_no_pending_archive_argument(self, bash, command):
        assert not assert_complete(bash, command, cwd="bsdtar")


@pytest.mark.bashcomp(
    ignore_env=r"^-declare -f _comp_cmd_tar$",
    pre_cmds=["tar() { printf 'bsdtar 3.8.9\\n'; }"],
)
class TestTarWithBsdtarVersion:
    @pytest.mark.complete("tar -tf ", cwd="tar")
    def test_archive_argument(self, completion):
        assert completion == "archive.tar.xz dir/ dir2/ escape.tar".split()


@pytest.mark.bashcomp(
    ignore_env=r"^-declare -f _comp_cmd_tar$",
    pre_cmds=["tar() { return 1; }"],
)
class TestTarWithoutVersion:
    @pytest.mark.complete("tar -tf ", cwd="tar")
    def test_archive_argument(self, completion):
        assert not completion
