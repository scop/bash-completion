import pytest


class TestPylint:
    @pytest.mark.complete("pylint --v", require_longopt=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pylint --confidence=HIGH,")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("pylint --help-msg=", require_longopt=True)
    def test_all_message_ids(self, completion):
        assert any("-" in x for x in completion)

    @pytest.mark.complete("pylint --disable=", require_longopt=True)
    def test_enabled_message_ids(self, completion):
        assert any("-" in x for x in completion)

    @pytest.mark.complete("pylint --enable=foo,", require_longopt=True)
    def test_disabled_message_ids(self, completion):
        assert any("-" in x for x in completion)
