import pytest


class TestPerl(object):

    @pytest.mark.complete("perl ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -e ")
    def test_2(self, completion):
        assert not completion.list

    @pytest.mark.complete("perl -V:install")
    def test_3(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -V::install")
    def test_4(self, completion):
        assert completion.list

    # Assume File::Spec and friends are always installed

    @pytest.mark.complete("perl -MFile")
    def test_5(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -MFile::Sp")
    def test_6(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -MFile::Spec::Func")
    def test_7(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -M-File")
    def test_8(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -m-File::")
    def test_9(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -")
    def test_10(self, completion):
        assert completion.list
