import pytest


class TestHtpasswd:

    @pytest.mark.complete("htpasswd ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("htpasswd -n htpasswd/ht")
    def test_2(self, completion):
        assert not completion.list

    @pytest.mark.complete("htpasswd ", cwd="htpasswd")
    def test_3(self, completion):
        assert completion.list == ["htpasswd"]

    @pytest.mark.complete("htpasswd -D htpasswd ", cwd="htpasswd")
    def test_4(self, completion):
        assert completion.list == "foo quux".split()
