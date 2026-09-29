import pytest


class TestVi:
    @pytest.mark.complete("vi ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("vi shared/ld.so.conf.d/")
    def test_2(self, completion):
        assert completion == "foo.txt libfoo.conf".split()
