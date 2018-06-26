import pytest


class Test(object):

    @pytest.mark.complete("xdg-mime ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-mime -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-mime query ")
    def test_query(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-mime query filetype ")
    def test_query_filetype(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-mime default foo.desktop ")
    def test_default(self, completion):
        assert completion.list

    @pytest.mark.complete("xdg-mime install --mode ")
    def test_install_mode(self, completion):
        assert completion.list
