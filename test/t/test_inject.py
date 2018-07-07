import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestInject(object):

    @pytest.mark.complete("inject ")
    def test_1(self, completion):
        assert completion.list
