import sys

import pytest

from conftest import assert_bash_exec


class TestUmount:
    @pytest.fixture(scope="class")
    def dummy_mnt(self, request, bash):
        """
        umount completion from fstab can't be tested directly because it
        (correctly) uses absolute paths. So we create a custom completion which
        reads from a file in our text fixture instead.
        """
        if sys.platform != "linux":
            pytest.skip("Linux specific")
        assert_bash_exec(bash, "unset COMPREPLY cur; unset -f _mnt_completion")
        assert_bash_exec(
            bash,
            "_mnt_completion() { "
            "local cur prev;_comp_get_words cur prev; "
            '_comp_cmd_umount__linux_fstab "$prev" < mount/test-fstab; '
            "} && complete -F _mnt_completion _mnt",
        )
        request.addfinalizer(
            lambda: assert_bash_exec(
                bash, "complete -r _mnt; unset -f _mnt_completion"
            )
        )

    @pytest.mark.complete("umount ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("_mnt /mnt/nice-test-p")
    def test_mnt_basic(self, completion, dummy_mnt):
        assert completion == "ath"

    # Note in tests below that return only one result, that the result
    # is shell unescaped due to how assert_complete handles the
    # "one result on same line case".

    @pytest.mark.complete(r"_mnt /mnt/nice\ test-p")
    def test_mnt_space(self, completion, dummy_mnt):
        assert completion == r"ath"

    @pytest.mark.complete(r"_mnt /mnt/nice\$test-p")
    def test_mnt_dollar(self, completion, dummy_mnt):
        assert completion == "ath"

    @pytest.mark.complete(r"_mnt /mnt/nice\ test\\p")
    def test_mnt_backslash(self, completion, dummy_mnt):
        assert completion == "ath"

    @pytest.mark.complete(r"_mnt /mnt/nice\ ")
    def test_mnt_after_space(self, completion, dummy_mnt):
        assert completion == sorted(
            (r"/mnt/nice\ test\\path", r"/mnt/nice\ test-path")
        )

    @pytest.mark.complete(r"_mnt /mnt/nice\$")
    def test_mnt_at_dollar(self, completion, dummy_mnt):
        assert completion == "test-path"

    @pytest.mark.complete(r"_mnt /mnt/nice\'")
    def test_mnt_at_quote(self, completion, dummy_mnt):
        assert completion == "test-path"

    @pytest.mark.complete("_mnt /mnt/other")
    def test_mnt_other(self, completion, dummy_mnt):
        assert completion == r"\'test\ path"

    @pytest.mark.complete("_mnt -L Ubu")
    def test_mnt_label_space(self, completion, dummy_mnt):
        assert completion == r"ntu\ Karmic"

    @pytest.mark.complete("_mnt -L Deb")
    def test_mnt_label_quote(self, completion, dummy_mnt):
        assert completion == r"ian-it\'s\ awesome"

    @pytest.mark.skipif(sys.platform != "linux", reason="Linux specific")
    def test_linux_fstab_unescape(self, bash):
        assert_bash_exec(bash, r"var=one\'two\\040three\\")
        assert_bash_exec(bash, "_comp_cmd_umount__linux_fstab_unescape var")
        output = assert_bash_exec(
            bash, r'printf "%s\n" "$var"', want_output=True
        )
        assert output.strip() == "one'two three\\"
        assert_bash_exec(bash, "unset var")
