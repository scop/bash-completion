#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from collections import defaultdict
from email.utils import formatdate
import sys
from textwrap import wrap

import git

repo = git.Repo('.')
changelog = defaultdict(list)

for id in repo.iter_commits('%s..HEAD' % sys.argv[1]):
    commit = repo.commit(id)
    if not commit.summary.startswith("Merge pull request "):
        changelog[commit.author.name].append(commit.summary)

print('bash-completion (X.Y)')
print('')

for author in sorted(changelog.keys()):
    print('  [ %s ]' % author)
    for log in changelog[author]:
        print('\n'.join(
            wrap(log, initial_indent='  * ', subsequent_indent='    ')))
    print('')

print(' -- Ville Skyttä <ville.skytta@iki.fi>  %s' %
      formatdate(localtime=True))
