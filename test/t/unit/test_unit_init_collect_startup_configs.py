import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, cwd="_comp__init_collect_startup_configs")
class TestUnitInitCollectStartupConfigs:
    def test_count(self, bash):
        assert_bash_exec(
            bash,
            "[[ ${_comp__test_startup__loading_order-} == 5 ]]",
        )

    @pytest.mark.parametrize(
        "module,expected",
        [
            ("quux", "host:1"),
            ("foo", "user:2"),
            ("bar", "user:3"),
            ("baz", "user:4"),
            ("qux", "user:5"),
        ],
    )
    def test_order(self, bash, module, expected):
        output = assert_bash_exec(
            bash,
            'echo "${_comp__test_startup__%s-}"' % module,
            want_output=True,
        )
        assert output.strip() == expected

    def test_masking(self, bash):
        output = assert_bash_exec(
            bash, 'echo "${_comp__test_startup__error-}"', want_output=True
        )
        assert output.strip() == ""
