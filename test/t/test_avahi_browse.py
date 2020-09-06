import pytest


@pytest.mark.bashcomp(
    cmd="avahi-browse",
)
class TestAvahiBrowse:
    @pytest.mark.complete("avahi-browse --", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("avahi-browse _", require_cmd=True)
    def test_service_types(self, completion):
        assert completion

    @pytest.mark.complete("avahi-browse -a _")
    def test_no_service_type_with_a(self, completion):
        assert not completion
