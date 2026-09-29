import pytest


class TestUsermod:
    @pytest.mark.complete("usermod ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("usermod -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("useradd --root shells -s ")
    def test_chroot_shells(self, completion):
        assert completion == "/bash/completion/canary"
