import pytest


class TestMfiUtil:
    @pytest.mark.complete("mfiutil -")
    def test_global_options(self, completion):
        assert completion

    @pytest.mark.complete("mfiutil show ")
    def test_show_subcommand(self, completion):
        assert completion

    @pytest.mark.complete("mfiutil show -")
    def test_options_after_subcommands(self, completion):
        assert not completion

    @pytest.mark.complete("mfiutil -e show dri")
    def test_show_drives_subcommand_with_global_option(self, completion):
        assert completion == ["ves"]

    @pytest.mark.complete("mfiutil locate 1 ")
    def test_locate_subcommand(self, completion):
        assert completion == ["off", "on"]
