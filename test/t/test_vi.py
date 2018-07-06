import pytest


class Test(object):

    @pytest.mark.complete("vi ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("vi shared/ld.so.conf.d/")
    def test_ld_so_conf_d(self, completion):
        assert completion.list == "foo.txt libfoo.conf".split()
