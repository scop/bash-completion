import pytest


@pytest.mark.bashcomp(
    cmd="pm-hibernate",
)
class TestPmHibernate(object):

    @pytest.mark.complete("pm-hibernate -")
    def test_1(self, completion):
        assert completion.list
