import pytest


class TestFind:
    @pytest.mark.complete("find ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("find -fstype ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("find -")
    def test_3(self, completion):
        assert completion

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("find -wholename ", cwd="shared/default")
    def test_4(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo foo.d/"]

    @pytest.mark.complete("find -uid ")
    def test_5(self, completion):
        assert not [x for x in completion if not x.isdigit()]

    @pytest.mark.complete("find -gid ")
    def test_6(self, completion):
        assert not [x for x in completion if not x.isdigit()]
