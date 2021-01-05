import os

import pytest


class TestChsh:
    @pytest.mark.complete("chsh ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chsh -s ")
    def test_shells(self, completion):
        if os.path.exists("/etc/shells"):
            assert completion
        else:
            assert not completion

    @pytest.mark.complete("chsh -", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("chsh --root shells -s ")
    def test_chroot_shells(self, completion):
        assert completion == "/bash/completion/canary"
