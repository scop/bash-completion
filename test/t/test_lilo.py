import pytest


class TestLilo:
    @pytest.mark.complete("lilo -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lilo -C lilo/lilo.conf -D ")
    def test_labels(self, completion):
        assert completion == sorted(
            "try 2.4.33 tamu PCDOS WinXP oldDOS".split()
        )

    @pytest.mark.complete("lilo -C -D ")
    def test_labels_incorrect_command(self, completion):
        assert not completion
