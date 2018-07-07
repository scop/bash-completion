import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestListOwners(object):

    @pytest.mark.complete("list_owners -")
    def test_1(self, completion):
        assert completion.list
