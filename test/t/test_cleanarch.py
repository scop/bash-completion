import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestCleanarch(object):

    @pytest.mark.complete("cleanarch -")
    def test_1(self, completion):
        assert completion.list
