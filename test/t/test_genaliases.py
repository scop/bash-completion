import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestGenaliases(object):

    @pytest.mark.complete("genaliases -")
    def test_1(self, completion):
        assert completion.list
