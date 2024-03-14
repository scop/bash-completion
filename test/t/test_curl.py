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

    @pytest.mark.complete("curl --proto-default ", require_cmd=True)
    def test_proto_default(self, completion):
        assert completion

    @pytest.mark.complete("curl --dont-fail-in-unset-mode")
    def test_unknown_option(self, completion):
        # Just see that it does not error out
        pass

    @pytest.mark.complete("curl --data-bina", require_cmd=True)
    def test_help_all_option(self, completion):
        """
        The option used as a canary here is one that should be available
        in all curl versions. It should be only listed in `--help all` output
        for curl versions that have their help output split to multiple
        categories (i.e. ones that support `--help all` to get the complete
        list), as well as the basic `--help` output for earlier versions that
        do not have that.
        """
        assert completion
