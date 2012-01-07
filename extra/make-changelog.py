#!/usr/bin/python
# -*- encoding: utf-8 -*-

import git
import sys
from collections import defaultdict
from textwrap import wrap
from email.Utils import formatdate

repo = git.Repo('.')
start = git.Commit(repo, sys.argv[1])
end = git.Commit(repo, 'HEAD')


curlog = repo.log(end)
oldlog = repo.log(start)

changelog = defaultdict(list)

for id in repo.commits_between(start, end):
    commit = git.Commit(repo, id)
    changelog[commit.author.name].append(commit.summary)

print 'bash-completion (X.Y)'
print

for author in sorted(changelog.keys()):
    print "  [ %s ]" % author
    for log in changelog[author]:
        print '\n'.join(wrap(log, initial_indent='  * ', subsequent_indent='    '))
    print

print ' -- David Paleino <d.paleino@gmail.com> ', formatdate(localtime=True)
