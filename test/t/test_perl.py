import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+PERL5LIB=")
class TestPerl:
    @pytest.mark.complete("perl ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("perl -e ")
    def test_2(self, completion):
        assert not completion

    @pytest.mark.complete("perl -V:install", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("perl -V::install", require_cmd=True)
    def test_4(self, completion):
        assert completion

    # Assume File::Spec and friends are always installed

    @pytest.mark.complete("perl -MFile", require_cmd=True)
    def test_5(self, completion):
        assert completion

    @pytest.mark.complete("perl -MFile::Sp", require_cmd=True)
    def test_6(self, completion):
        assert completion

    @pytest.mark.complete("perl -MFile::Spec::Func", require_cmd=True)
    def test_7(self, completion):
        assert completion

    @pytest.mark.complete("perl -M-File", require_cmd=True)
    def test_8(self, completion):
        assert completion

    @pytest.mark.complete("perl -m-File::", require_cmd=True)
    def test_9(self, completion):
        assert completion

    @pytest.mark.complete("perl -")
    def test_10(self, completion):
        assert completion

    @pytest.mark.complete("perl foo shared/default/f")
    def test_11(self, completion):
        """Second arg should complete files+dirs."""
        assert completion == "foo foo.d/".split()

    @pytest.mark.complete("perl -Ishared/default/")
    def test_12(self, completion):
        """-I without space should complete dirs."""
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("perl -I shared/default/")
    def test_13(self, completion):
        """-I with space should complete dirs."""
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("perl -xshared/default/b")
    def test_14(self, completion):
        """-x without space should complete dirs."""
        assert completion == r"ar\ bar.d/"

    @pytest.mark.complete("perl -x shared/default/b")
    def test_15(self, completion):
        """-x with space should complete files+dirs."""
        assert completion == ["bar", "bar bar.d/"]

    @pytest.mark.complete(
        "perl -d:", env=dict(PERL5LIB="$PWD/perl"), require_cmd=True
    )
    def test_16(self, completion):
        assert "BashCompletion" in completion

    @pytest.mark.complete(
        "perl -dt:", env=dict(PERL5LIB="$PWD/perl"), require_cmd=True
    )
    def test_17(self, completion):
        assert "BashCompletion" in completion

    @pytest.mark.complete("perl -E ")
    def test_dash_capital_e(self, completion):
        assert not completion

    @pytest.mark.complete("perl -e")
    def test_dash_e(self, completion):
        assert not completion
