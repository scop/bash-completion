import pytest


class Test(object):

    @pytest.mark.complete("mkisofs ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("mkisofs -uid ")
    def test_uid(self, completion):
        assert not [x for x in completion.list if not x.isdigit()]

    @pytest.mark.complete("mkisofs -gid ")
    def test_gid(self, completion):
        assert not [x for x in completion.list if not x.isdigit()]
