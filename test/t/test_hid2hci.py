import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/lib/udev',
)
class Test(object):

    @pytest.mark.complete("hid2hci -")
    def test_dash(self, completion):
        assert completion.list
