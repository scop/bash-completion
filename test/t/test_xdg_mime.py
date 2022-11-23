import pytest


@pytest.mark.bashcomp(cmd="xdg-mime")
class TestXdgMime:
    @pytest.mark.complete("xdg-mime ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime query ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime query filetype ")
    def test_4(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime default foo.desktop ", require_cmd=True)
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime install --mode ")
    def test_6(self, completion):
        assert completion

    @pytest.mark.complete("xdg-mime query filetype foo ")
    def test_filetype_one_arg(self, completion):
        assert not completion
