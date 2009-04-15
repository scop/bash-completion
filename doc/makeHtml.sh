#!/bin/bash -eu

[ -d html~ ] || mkdir html~
a2x -D html~ -d book -f xhtml main.txt
