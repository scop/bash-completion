import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestMailmanctl(object):

    @pytest.mark.complete("mailmanctl ")
    def test_1(self, completion):
        assert completion.list
