import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class TestDumpdb(object):

    @pytest.mark.complete("dumpdb ")
    def test_1(self, completion):
        assert completion.list
