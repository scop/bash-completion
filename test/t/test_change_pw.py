import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestChangePw(object):

    @pytest.mark.complete("change_pw -")
    def test_1(self, completion):
        assert completion.list
