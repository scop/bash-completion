#!/usr/bin/python
# -*- encoding: utf-8 -*-

import git
import sys
from collections import defaultdict
from textwrap import wrap
from email.Utils import formatdate

repo = git.Repo('.')
changelog = defaultdict(list)

for id in repo.iter_commits('%s..HEAD' % sys.argv[1]):
    commit = repo.commit(id)
    changelog[commit.author.name].append(commit.summary)

print 'bash-completion (X.Y)'
print

for author in sorted(changelog.keys()):
    print "  [ %s ]" % author
    for log in changelog[author]:
        print '\n'.join(wrap(log, initial_indent='  * ', subsequent_indent='    '))
    print

print ' -- David Paleino <d.paleino@gmail.com> ', formatdate(localtime=True)
