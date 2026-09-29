import pytest


class TestHtpasswd:
    @pytest.mark.complete("htpasswd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("htpasswd -n htpasswd/ht")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("htpasswd ", cwd="htpasswd")
    def test_3(self, completion):
        assert completion == "htpasswd"

    @pytest.mark.complete("htpasswd -D htpasswd ", cwd="htpasswd")
    def test_4(self, completion):
        assert completion == "foo quux".split()

    @pytest.mark.complete("htpasswd -", require_cmd=True)
    def test_5(self, completion):
        assert completion
