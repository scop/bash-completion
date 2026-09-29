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

    @pytest.mark.complete("find -wholename ", cwd="shared/default")
    def test_4(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("find -uid ")
    def test_5(self, completion):
        assert not [x for x in completion if not x.isdigit()]

    @pytest.mark.complete("find -gid ")
    def test_6(self, completion):
        assert not [x for x in completion if not x.isdigit()]

    @pytest.mark.complete("find -exec shared/bin/ar")
    def test_exec(self, completion):
        assert completion == "p"

    # sh +: something that produces completions also when command is not
    #       available, and the chosen completion is not one of find's
    @pytest.mark.complete("find /some/where -exec sh +")
    def test_exec_args(self, completion):
        assert "+o" in completion
