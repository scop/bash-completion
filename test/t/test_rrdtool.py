import pytest


class TestRrdtool:
    @pytest.mark.complete("rrdtool ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rrdtool info rrdtool/")
    def test_info_first_arg(self, completion):
        assert completion
        assert all(x.endswith(".rrd") for x in completion)

    @pytest.mark.complete("rrdtool info rrdtool/test.rrd")
    def test_info_with_all_args(self, completion):
        assert not completion

    @pytest.mark.complete("rrdtool dump rrdtool/")
    def test_dump_first_arg(self, completion):
        assert completion
        assert all(x.endswith(".rrd") for x in completion)

    @pytest.mark.complete("rrdtool dump rrdtool/test.rrd rrdtool/")
    def test_dump_second_arg(self, completion):
        assert completion
        assert all(x.endswith(".xml") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/")
    def test_restore_first_arg(self, completion):
        assert completion
        assert all(x.endswith(".xml") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/test.xml")
    def test_restore_second_arg(self, completion):
        assert all(x.endswith(".rrd") for x in completion)

    @pytest.mark.complete("rrdtool restore --force rrdtool/")
    def test_restore_with_leading_option(self, completion):
        assert completion
        assert all(x.endswith(".xml") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/test.xml -f")
    def test_restore_second_arg_with_trailing_option(self, completion):
        assert all(x.endswith(".rrd") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/test.xml rrdtool/test.rrd")
    def test_restore_with_all_args(self, completion):
        assert not completion

    @pytest.mark.complete("rrdtool restore rrdtool/test.xml rrdtool/test.rrd -f")
    def test_restore_with_all_args_and_option(self, completion):
        assert not completion
