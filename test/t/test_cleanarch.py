import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class Test(object):

    @pytest.mark.complete("cleanarch -")
    def test_dash(self, completion):
        assert completion.list
