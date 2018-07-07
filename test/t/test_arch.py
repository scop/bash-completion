import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestArch(object):

    @pytest.mark.complete("arch -")
    def test_1(self, completion):
        assert completion.list
