import fnmatch
import os

import pytest


class TestUpgradepkg:
    @pytest.mark.complete("upgradepkg -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("upgradepkg --")
    def test_2(self, completion):
        assert (
            completion
            == "--dry-run --install-new --reinstall --verbose".split()
        )

    @pytest.mark.complete("upgradepkg ", cwd="slackware/home")
    def test_4(self, completion):
        expected = sorted(
            [
                "%s/" % x
                for x in os.listdir("slackware/home")
                if os.path.isdir("./slackware/home/%s" % x)
            ]
            + [
                x
                for x in os.listdir("slackware/home")
                if os.path.isfile("./slackware/home/%s" % x)
                and fnmatch.fnmatch(x, "*.t[bglx]z")
            ]
        )
        assert completion == expected

    @pytest.mark.complete("upgradepkg foo%", cwd="slackware/home")
    def test_after_percent(self, completion):
        expected = sorted(
            [
                "%s/" % x
                for x in os.listdir("slackware/home")
                if os.path.isdir("./slackware/home/%s" % x)
            ]
            + [
                x
                for x in os.listdir("slackware/home")
                if os.path.isfile("./slackware/home/%s" % x)
                and fnmatch.fnmatch(x, "*.t[bglx]z")
            ]
        )
        assert completion == ["foo%%%s" % x for x in expected]
