from shlex import quote

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(cmd="alternatives", temp_cwd=True)
class TestAlternatives:
    @pytest.fixture
    def files(self, tmp_path):
        (tmp_path / "groups").mkdir()
        (tmp_path / "groups" / "fixture-group").touch()
        (tmp_path / "fixture-file").touch()
        (tmp_path / "fixture-dir").mkdir()
        return tmp_path

    def complete(self, bash, files, operands, kind, admin="groups"):
        expected = {
            "file": ["fixture-dir/", "fixture-file"],
            "name": "-group",
            "directory": "-dir/",
            "none": [],
        }
        command = f"alternatives --admindir {quote(admin)} {operands} fixture"
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(files))
            assert assert_complete(bash, command) == expected[kind]

    @pytest.mark.parametrize(
        "operands,kind",
        [
            ("--install", "file"),
            ("--install /link", "name"),
            ("--install /link name", "file"),
            ("--install /link name /target", "none"),
            ("--family", "none"),
            ("--initscript", "none"),
            ("--altdir", "directory"),
            ("--admindir", "directory"),
            ("--auto", "name"),
            ("--display", "name"),
            ("--config", "name"),
            ("--remove-all", "name"),
        ],
    )
    def test_operands(self, bash, files, operands, kind):
        self.complete(bash, files, operands, kind)

    @pytest.mark.parametrize("option", ("--remove", "--set"))
    @pytest.mark.parametrize("tail,kind", (("", "name"), ("name", "file")))
    def test_two_operands(self, bash, files, option, tail, kind):
        self.complete(bash, files, f"{option} {tail}", kind)

    @pytest.mark.parametrize("option", ("--follower", "--slave"))
    @pytest.mark.parametrize(
        "tail,kind", (("", "file"), ("/link", "name"), ("/link name", "file"))
    )
    def test_follower(self, bash, files, option, tail, kind):
        self.complete(bash, files, f"{option} {tail}", kind)

    @pytest.mark.parametrize("option", ("--add-follower", "--add-slave"))
    @pytest.mark.parametrize(
        "tail,kind",
        (
            ("", "name"),
            ("name", "file"),
            ("name /target", "file"),
            ("name /target /link", "name"),
            ("name /target /link name", "file"),
        ),
    )
    def test_add_follower(self, bash, files, option, tail, kind):
        self.complete(bash, files, f"{option} {tail}", kind)

    @pytest.mark.parametrize("option", ("--remove-follower", "--remove-slave"))
    @pytest.mark.parametrize(
        "tail,kind", (("", "name"), ("name", "file"), ("name /target", "name"))
    )
    def test_remove_follower(self, bash, files, option, tail, kind):
        self.complete(bash, files, f"{option} {tail}", kind)

    @pytest.mark.parametrize(
        "prefix",
        (
            "--install /link name /target 1 --family family --slave",
            "--family family --install /link name /target 1 --follower",
            "--install /link name /target 1 --initscript service --follower",
            "--initscript service --install /link name /target 1 --slave",
            "--install /link name /target 1 --test --slave",
            "--install /link name /target 1 --verbose --slave",
            "--install /link name /target 1 --keep-missing --slave",
            "--install /link name /target 1 --keep-foreign --slave",
            "--install /link name /target 1 --altdir /links --follower",
            "--install /link name /target 1 --admindir groups --slave",
            "--follower /first first /target "
            "--install /link name /target 1 --family family --follower",
            "--family family --follower /first first /target "
            "--install /link name /target 1 --slave",
        ),
    )
    @pytest.mark.parametrize(
        "tail,kind", (("", "file"), ("/link", "name"), ("/link name", "file"))
    )
    def test_reordered_options(self, bash, files, prefix, tail, kind):
        self.complete(bash, files, f"{prefix} {tail}", kind)

    @pytest.mark.parametrize(
        "operands",
        (
            "--install /link --family /target 1 --slave /link",
            "--family --install --install /link name /target 1 --slave /link",
            "--family --admindir --install /link name /target 1 --slave /link",
            "--initscript --slave --install /link name /target 1 "
            "--slave /link",
            "--install /link --admindir /target 1 --slave /link",
        ),
    )
    def test_option_like_operands(self, bash, files, operands):
        self.complete(bash, files, operands, "name")

    @pytest.mark.parametrize(
        "operands",
        (
            "--add-follower --family /target /link "
            "--admindir /target --admindir",
            "--remove-follower --family /target --admindir --admindir",
        ),
    )
    def test_option_like_follower_operands(self, bash, files, operands):
        self.complete(bash, files, operands, "directory")

    def test_admindir_after_option_like_name(self, bash, files):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(files))
            command = (
                "alternatives --install /link --admindir /target 1 "
                "--admindir groups --slave /link fixture"
            )
            assert assert_complete(bash, command) == "-group"

    @pytest.mark.parametrize("admin", ("groups", "groups with spaces"))
    def test_last_admindir(self, bash, files, admin):
        (files / "first-groups").mkdir()
        (files / "first-groups" / "wrong-group").touch()
        if admin != "groups":
            (files / "groups").rename(files / admin)
        operands = f"--admindir {quote(admin)} --display"
        self.complete(bash, files, operands, "name", admin="first-groups")

    @pytest.mark.parametrize("option", ("--help", "--usage", "--version"))
    def test_terminal_option(self, bash, files, option):
        self.complete(bash, files, option, "none")

    @pytest.mark.parametrize(
        "operands",
        (
            "--install /link name /target 1",
            "--install /link name /target 1 --family family",
            "--install /link name /target 1 --initscript service",
        ),
    )
    def test_options_after_operands(self, bash, files, operands):
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(files))
            completion = assert_complete(
                bash,
                f"alternatives {operands} --",
                skipif="! type alternatives &>/dev/null",
            )
            assert "--family" in completion
            assert "--follower" in completion

    def test_empty_admindir_does_not_fall_back(self, bash, files):
        defaults = files / "defaults" / "alternatives"
        defaults.mkdir(parents=True)
        (defaults / "fixture-group").touch()
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(files))
            bash_env.write_variable(
                "_comp_test_definition",
                "$(declare -f _comp_cmd_alternatives__installed)",
                quote=False,
            )
            # Redirect only the default-directory probe to an owned fixture;
            # the host need not have /var/lib/alternatives or root access.
            assert_bash_exec(
                bash,
                r'eval "${_comp_test_definition//\/var\/lib\//defaults/}"',
            )
            try:
                assert (
                    assert_complete(bash, "alternatives --display fixture")
                    == "-group"
                )
                assert (
                    assert_complete(
                        bash, "alternatives --admindir '' --display fixture"
                    )
                    == []
                )
            finally:
                assert_bash_exec(bash, 'eval "$_comp_test_definition"')
