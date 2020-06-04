import pytest


class TestCurl:
    @pytest.mark.complete("curl --h", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("curl -o f", cwd="shared/default/foo.d")
    def test_2(self, completion):
        assert completion == "oo"

    @pytest.mark.complete("curl -LRo f", cwd="shared/default/foo.d")
    def test_3(self, completion):
        assert completion == "oo"

    @pytest.mark.complete("curl --o f")
    def test_4(self, completion):
        assert not completion

    @pytest.mark.complete("curl --data @", cwd="shared/default/foo.d")
    def test_data_atfile(self, completion):
        assert completion == "foo"

    @pytest.mark.complete("curl --data @foo.", cwd="shared/default")
    def test_data_atfile_dir(self, completion):
        assert completion == "d/"
        assert not completion.endswith(" ")
