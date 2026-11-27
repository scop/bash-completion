import shlex

import pytest

from conftest import assert_complete


class TestAptitude:
    @pytest.fixture
    def apt_cache_path(self, tmp_path):
        script = tmp_path / "apt-cache"
        script.write_text(
            """#!/bin/bash
case "$*" in
    '--no-generate pkgnames '*)
        names=(demo-real backup-real)
        ;;
    '--no-generate --all-names pkgnames '*)
        names=(demo-real demo-virtual+1.2 demo-virtual+1.2 demo-virtual:any
               demo-missing
               backup-real backup-virtual)
        ;;
    '-o APT::Cache::Generate=false -o APT::Cache::GivenOnly=true dotty '*)
        [[ $LC_ALL == C ]] || exit 1
        shift 5
        printf 'digraph packages {\\n'
        for name; do
            case $name in
                demo-virtual+1.2)
                    printf '"%s" [shape=triangle];\\n' "$name" "$name"
                    ;;
                demo-missing)
                    printf '"%s" [shape=hexagon];\\n' "$name"
                    ;;
                backup-virtual)
                    printf '"%s" [shape=triangle];\\n' "$name"
                    printf 'incomplete graph\\n' >&2
                    exit 1
                    ;;
                *) exit 1 ;;
            esac
        done
        printf '}\\n'
        exit 0
        ;;
    *) exit 1 ;;
esac
prefix=${!#}
for name in "${names[@]}"; do
    [[ $name == "$prefix"* ]] && printf '%s\\n' "$name"
done
exit 0
"""
        )
        script.chmod(0o755)
        return f"{shlex.quote(str(tmp_path))}:$PATH"

    @pytest.mark.parametrize(
        ("arguments", "expected"),
        [
            ("install demo-", ["demo-real", "demo-virtual+1.2"]),
            ("install demo-virtual+1.", "2"),
            ("install demo-mis", []),
            ("install demo-re", "al"),
            ("install backup-", "real"),
            ("install ", ["backup-real", "demo-real"]),
            ("show demo-", "real"),
        ],
    )
    def test_virtual_install_packages(
        self, bash, apt_cache_path, arguments, expected
    ):
        assert (
            assert_complete(
                bash, f"aptitude {arguments}", env={"PATH": apt_cache_path}
            )
            == expected
        )

    @pytest.mark.complete("aptitude ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("aptitude -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("aptitude --", require_cmd=True)
    def test_long_options(self, completion):
        assert completion

    @pytest.mark.complete("aptitude -u -")
    def test_no_i_with_u(self, completion):
        assert "-i" not in completion

    @pytest.mark.complete("aptitude -i -")
    def test_no_u_with_i(self, completion):
        assert "-u" not in completion
