import pytest


class TestCarton:
    @pytest.mark.complete("carton ", require_cmd=True)
    def test_commands(self, completion):
        assert all(x in completion for x in "help install".split())

    @pytest.mark.complete("carton install -", require_cmd=True)
    def test_install_options(self, completion):
        assert all(x in completion for x in "--cached --help".split())
