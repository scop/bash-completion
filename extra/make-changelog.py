#!/usr/bin/python3

import sys
from collections import defaultdict
from email.utils import formatdate
from textwrap import wrap
from typing import Dict, List

import git

repo = git.Repo(".")
changelog = defaultdict(list)  # type: Dict[str, List[str]]

if len(sys.argv) != 2:
    print("Usage: %s SINCE-TAG" % __file__, file=sys.stderr)
    sys.exit(2)

for id in repo.iter_commits("%s..HEAD" % sys.argv[1]):
    commit = repo.commit(id)
    if not commit.summary.startswith("Merge pull request "):
        changelog[commit.author.name].append(commit.summary)

print("bash-completion (X.Y)")
print("")

for author in sorted(changelog.keys()):
    print("  [ %s ]" % author)
    for log in changelog[author]:
        print(
            "\n".join(
                wrap(log, initial_indent="  * ", subsequent_indent="    ")
            )
        )
    print("")

print(
    " -- Ville Skyttä <ville.skytta@iki.fi>  %s" % formatdate(localtime=True)
)
