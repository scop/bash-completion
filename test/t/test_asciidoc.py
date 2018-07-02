import pytest


class Test(object):

    @pytest.mark.complete("asciidoc ")
    def test_(self, completion):
        assert completion.list
