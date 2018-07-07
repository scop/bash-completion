import pytest


class TestAsciidoc(object):

    @pytest.mark.complete("asciidoc ")
    def test_1(self, completion):
        assert completion.list
