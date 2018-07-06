import pytest


class Test(object):

    @pytest.mark.complete("acroread ", cwd="fixtures/acroread")
    def test_(self, completion):
        assert completion.list == "foo.d/ t.pdf".split()
