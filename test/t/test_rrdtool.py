import pytest


class TestRrdtool:
    @pytest.mark.complete("rrdtool ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rrdtool dump rrdtool/")
    def test_dump(self, completion):
        assert completion
        assert all(x.endswith(".rrd") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/")
    def test_restore(self, completion):
        assert completion
        assert all(x.endswith(".xml") for x in completion)

    @pytest.mark.complete("rrdtool restore --force rrdtool/")
    def test_restore_with_option(self, completion):
        assert completion
        assert all(x.endswith(".xml") for x in completion)

    @pytest.mark.complete("rrdtool restore rrdtool/test.xml")
    def test_restore_with_xml(self, completion):
        assert not completion
