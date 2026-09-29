import pytest


@pytest.mark.bashcomp(cmd="qemu-system-x86_64")
class TestQemuSystemX8664:
    @pytest.mark.complete("qemu-system-x86_64 ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("qemu-system-x86_64 -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("qemu-system-x86_64 -k ", require_cmd=True)
    def test_keymaps(self, completion):
        assert any(x.lower().startswith("en") for x in completion)
