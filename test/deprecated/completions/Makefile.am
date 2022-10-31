EXTRA_DIST = \
	adb \
	cal \
	chfn \
	chsh \
	dmesg \
	eject \
	hexdump \
	hwclock \
	ionice \
	look \
	mock \
	modules \
	mount \
	mount.linux \
	newgrp \
	nmcli \
	op \
	renice \
	repomanage \
	reptyr \
	rfkill \
	rtcwake \
	runuser \
	slackpkg \
	su \
	svn \
	svnadmin \
	svnlook \
	udevadm \
	umount \
	umount.linux \
	write \
	xm \
	yum

update:
	for f in *; do \
		case $$f in \
			Makefile*|README.md) ;; \
			*) git rm -f $$f ;; \
		esac \
	done
	for f in ../../../completions/_*; do \
		ln -sf $$f $${f##*/_}; \
		git add $${f##*/_}; \
	done
