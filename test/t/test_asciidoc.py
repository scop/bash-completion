import pytest


class TestAsciidoc:

    @pytest.mark.complete("asciidoc ")
    def test_1(self, completion):
        assert completion.list
