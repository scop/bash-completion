#!/bin/bash

if [ -n "$1" ]; then
	[ "$1" == "--debug" ] && set -x
fi

CHANGES="./Changelog"
AUTHOR="$NAME"
[ -n "$EMAIL" ] || EMAIL="`whoami`@`hostname`"

[ -r "$CHANGES" ] || touch $CHANGES

wrap() {
	echo "$@" | fold --spaces --width=80
}

section=
started=0
header="^bash-completion \(([:digit:]+.*)\)"
maint="  \[ ([[:alpha:][:blank:]]+) \]"
trailer=" -- ([[:alpha:][:blank:]]+) <([^>]+)>  (.*)"

IFS=$'\n'
for line in $(cat $CHANGES)
do
	if [[ "$line" =~ $header ]]; then
		if [ $started -eq 0 ]; then
			started=1
			section="$line"
		else
			break
		fi
	elif [[ "$line" =~ $maint ]]; then
		section="$section\n\n$line"
	elif [[ "$line" =~ $trailer ]]; then
		break
	else
		section="$section\n$line"
	fi
done

# weird hack, really.
lines=$(echo -e $section | wc -l)
final=$(($lines - 1))

echo -e "$section" | tail -$final
