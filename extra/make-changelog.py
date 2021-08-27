#!/usr/bin/env python3

from datetime import date

import git  # type: ignore[import]

repo = git.Repo(".")
current_tag_name = None
previous_tag_name = None

for tag in list(
    sorted(repo.tags, key=lambda tag: -tag.commit.committed_date)
) + [None]:
    if tag:
        current_tag_name = tag.name
        current_tag_date = str(date.fromtimestamp(tag.commit.committed_date))
    else:
        current_tag_name = "49e7b957815a3ba0972c4a0d979132d6e7a549c6"
        current_tag_date = "2000-08-08"
    if "-alt" in current_tag_name:
        continue
    if not previous_tag_name:
        previous_tag_name = current_tag_name
        previous_tag_date = current_tag_date
        continue
    if previous_tag_name.startswith("rel200"):
        datestamp = ""
    else:
        datestamp = f" ({previous_tag_date})"
    print(
        "## %s%s"
        % (
            previous_tag_name.lstrip("rel"),
            datestamp,
        )
    )
    print("")
    for commit in reversed(
        list(repo.iter_commits(f"{current_tag_name}..{previous_tag_name}"))
    ):
        message = commit.message.strip().splitlines()[0].lstrip(" -*")
        print(
            "* %s ([%s](https://www.github.com/scop/bash-completion/commit/%s))"
            % (
                message,
                commit.hexsha[:7],
                commit.hexsha,
            )
        )
    print("")
    previous_tag_name = current_tag_name
    previous_tag_date = current_tag_date
