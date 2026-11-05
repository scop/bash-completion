import pytest


class TestDig:
    @pytest.mark.complete("dig -")
    def test_flags(self, completion):
        assert completion

    @pytest.mark.complete("dig +")
    def test_plus_options(self, completion):
        assert completion

    @pytest.mark.complete("dig +nore", require_cmd=True)
    def test_plus_norecurse(self, completion):
        assert "+norecurse" in completion

    @pytest.mark.complete("dig -t ")
    def test_type_after_flag(self, completion):
        assert "A" in completion
        assert "SOA" in completion

    @pytest.mark.complete("dig -c ")
    def test_class_after_flag(self, completion):
        assert "IN" in completion
        assert "NONE" in completion
        assert "ANY" in completion

    @pytest.mark.complete("dig @9.9.9.9. C", require_cmd=True)
    def test_class_after_at_server(self, completion):
        assert "CH" in completion
        assert "CNAME" in completion

    @pytest.mark.complete("dig @9.9.9.9. NS ", require_cmd=True)
    def test_after_at_server_type_only_class_not_rr_types(self, completion):
        assert "IN" in completion
        assert "SOA" not in completion

    @pytest.mark.complete("dig C", require_cmd=True)
    def test_bare_class_or_type_without_at(self, completion):
        assert "CH" in completion
        assert "CNAME" in completion

    @pytest.mark.complete("dig CH TXT @9.9.9.9. ", require_cmd=True)
    def test_chaos_txt_after_server(self, completion):
        assert "version.bind" in completion
        assert "version.server" in completion

    @pytest.mark.complete("dig CH TXT @9.9.9.9. +norec ", require_cmd=True)
    def test_chaos_txt_after_server_plus_opt(self, completion):
        assert "version.bind" in completion
        assert "hostname.bind" in completion

    @pytest.mark.complete("dig CHAOS @9.9.9.9. TXT +norecurse ", require_cmd=True)
    def test_chaos_txt_class_at_server_type_plus(self, completion):
        assert "id.server" in completion
        assert "version.bind" in completion

    @pytest.mark.complete("dig SO")
    def test_bare_type(self, completion):
        assert "SOA" in completion

    @pytest.mark.complete("dig CH TXT ", require_cmd=True)
    def test_chaos_txt_names_ch_txt(self, completion):
        assert "version.bind" in completion
        assert "hostname.bind" in completion
        assert "id.server" in completion

    @pytest.mark.complete("dig chaos txt ", require_cmd=True)
    def test_chaos_txt_names_lowercase(self, completion):
        assert "authors.bind" in completion
        assert "version.server" in completion

    @pytest.mark.complete("dig -c CH -t TXT ", require_cmd=True)
    def test_chaos_txt_names_flags(self, completion):
        assert "version.bind" in completion

    @pytest.mark.complete("dig -t A -t ")
    def test_second_type_flag_suppressed(self, completion):
        assert "SOA" not in completion

    @pytest.mark.complete("dig A -t ")
    def test_type_after_bare_type_second_flag_suppressed(self, completion):
        assert "SOA" not in completion

    @pytest.mark.complete("dig -c IN -c ")
    def test_second_class_flag_suppressed(self, completion):
        assert "CH" not in completion

    @pytest.mark.complete("dig A ")
    def test_bare_only_class_after_type(self, completion):
        assert "IN" in completion
        assert "SOA" not in completion

    @pytest.mark.complete("dig IN ")
    def test_bare_only_type_after_class(self, completion):
        assert "SOA" in completion
        assert "CH" not in completion

    @pytest.mark.complete("dig myunknownhostxyz123")
    def test_bare_partial_name_uses_known_hosts(self, completion):
        assert "SOA" not in completion

    @pytest.mark.complete("dig example.com ")
    def test_after_dotted_name_suggest_class_and_type(self, completion):
        assert "IN" in completion
        assert "SOA" in completion

    @pytest.mark.complete("dig example.com NS ")
    def test_after_name_and_type_suggest_class_only(self, completion):
        assert "IN" in completion
        assert "SOA" not in completion

    @pytest.mark.complete("dig CHAOS @9.9.9.9. -t TXT ", require_cmd=True)
    def test_chaos_txt_names_mixed_bare_and_flag(self, completion):
        assert "version.bind" in completion
