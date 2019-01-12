import pytest


class TestInotifywatch:

    @pytest.mark.complete("inotifywatch ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("inotifywatch --")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("inotifywatch -e ")
    def test_3(self, completion):
        assert len(completion.list) > 1
