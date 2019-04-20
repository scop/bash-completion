import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/lib/udev:$PATH",))
class TestHid2hci:
    @pytest.mark.complete("hid2hci -")
    def test_1(self, completion):
        assert completion
