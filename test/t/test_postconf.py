import pytest


class TestPostconf:
    @pytest.mark.complete("postconf -", require_cmd=True)
    def test_1(self, completion):
        assert len(completion) > 1

    # Broken configs may abort output of postconf halfway through, so use
    # something from early output to not trigger false positives because of
    # this. For example, inet_protocols=all but no IPv6 configured:
    # postconf: fatal: parameter inet_interfaces: no local interface found
    #                  for ::1
    # ...and output can be cut off somewhere near lmtp_tls_secur*.
    # ...or be completely missing, so all we can do is to skip.
    @pytest.mark.complete(
        "postconf al", require_cmd=True, xfail="! postconf &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
