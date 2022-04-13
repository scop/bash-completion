import pytest


@pytest.mark.bashcomp(
    cmd="avahi-browse",
)
class TestAvahiBrowse:
    @pytest.mark.complete("avahi-browse --", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete(
        "avahi-browse _",
        require_cmd=True,
        xfail='test ! "$(avahi-browse --dump-db 2>/dev/null)"',
    )
    def test_service_types(self, completion):
        assert completion

    @pytest.mark.complete("avahi-browse -a _")
    def test_no_service_type_with_a(self, completion):
        assert not completion

    @pytest.mark.complete("avahi-browse --dont-fail-in-unset-mode")
    def test_unknown_option(self, completion):
        # Just see that it does not error out
        pass
