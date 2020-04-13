import pytest


class TestCpio:
    @pytest.mark.complete("cpio --")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cpio -R ")
    def test_2(self, bash, completion, output_sort_uniq):
        users = output_sort_uniq("compgen -u")
        assert completion == users
