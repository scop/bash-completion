import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/lib/udev',
)
class TestHid2hci(object):

    @pytest.mark.complete("hid2hci -")
    def test_1(self, completion):
        assert completion.list
