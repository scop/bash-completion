SUBDIRS = test

sysconf_DATA = bash_completion

bashcompdir = $(sysconfdir)/bash_completion.d
bashcomp_DATA = contrib/abook \
		contrib/ant \
		contrib/apache2ctl \
		contrib/apt \
		contrib/apt-build \
		contrib/aptitude \
		contrib/aspell \
		contrib/autorpm \
		contrib/bash-builtins \
		contrib/bind-utils \
		contrib/bitkeeper \
		contrib/bittorrent \
		contrib/bluez \
		contrib/brctl \
		contrib/bzip2 \
		contrib/cardctl \
		contrib/cfengine \
		contrib/chkconfig \
		contrib/chsh \
		contrib/cksfv \
		contrib/clisp \
		contrib/configure \
		contrib/coreutils \
		contrib/cowsay \
		contrib/cpan2dist \
		contrib/cpio \
		contrib/cups \
		contrib/cryptsetup \
		contrib/cvs \
		contrib/cvsps \
		contrib/dd \
		contrib/dhclient \
		contrib/dict \
		contrib/dpkg \
		contrib/dselect \
		contrib/dsniff \
		contrib/findutils \
		contrib/freeciv \
		contrib/fuse \
		contrib/gcc \
		contrib/gcl \
		contrib/gdb \
		contrib/genisoimage \
		contrib/getent \
		contrib/gkrellm \
		contrib/gnatmake \
		contrib/gpg \
		contrib/gpg2 \
		contrib/gzip \
		contrib/heimdal \
		contrib/hping2 \
		contrib/iconv \
		contrib/imagemagick \
		contrib/info \
		contrib/iptables \
		contrib/ipmitool \
		contrib/ipv6calc \
		contrib/isql \
		contrib/jar \
		contrib/java \
		contrib/k3b \
		contrib/kldload \
		contrib/larch \
		contrib/ldapvi \
		contrib/lftp \
		contrib/lilo \
		contrib/links \
		contrib/lintian \
		contrib/lisp \
		contrib/lvm \
		contrib/lzma \
		contrib/lzop \
		contrib/mailman \
		contrib/make \
		contrib/man \
		contrib/mc \
		contrib/mcrypt \
		contrib/mdadm \
		contrib/medusa \
		contrib/minicom \
		contrib/mkinitrd \
		contrib/module-init-tools \
		contrib/monodevelop \
		contrib/mount \
		contrib/mplayer \
		contrib/msynctool \
		contrib/mtx \
		contrib/munin-node \
		contrib/mutt \
		contrib/mysqladmin \
		contrib/ncftp \
		contrib/net-tools \
		contrib/nmap \
		contrib/ntpdate \
		contrib/openldap \
		contrib/openssl \
		contrib/p4 \
		contrib/perl \
		contrib/pine \
		contrib/pkg-config \
		contrib/pkg_install \
		contrib/pkgtools \
		contrib/pm-utils \
		contrib/portupgrade \
		contrib/postfix \
		contrib/postgresql \
		contrib/povray \
		contrib/python \
		contrib/qdbus \
		contrib/qemu \
		contrib/quota-tools \
		contrib/rcs \
		contrib/rdesktop \
		contrib/reportbug \
		contrib/resolvconf \
		contrib/rfkill \
		contrib/ri \
		contrib/rpcdebug \
		contrib/rpm \
		contrib/rpmcheck \
		contrib/rrdtool \
		contrib/rsync \
		contrib/rtcwake \
		contrib/samba \
		contrib/sbcl \
		contrib/screen \
		contrib/service \
		contrib/shadow \
		contrib/sitecopy \
		contrib/smartctl \
		contrib/snownews \
		contrib/ssh \
		contrib/sshfs \
		contrib/strace \
		contrib/svk \
		contrib/sysctl \
		contrib/sysv-rc \
		contrib/tar \
		contrib/tcpdump \
		contrib/unace \
		contrib/unrar \
		contrib/update-alternatives \
		contrib/util-linux \
		contrib/vncviewer \
		contrib/vpnc \
		contrib/wireless-tools \
		contrib/wodim \
		contrib/wtf \
		contrib/wvdial \
		contrib/xhost \
		contrib/xm \
		contrib/xmllint \
		contrib/xmlwf \
		contrib/xmms \
		contrib/xrandr \
		contrib/xsltproc \
		contrib/xz \
		contrib/yp-tools \
		contrib/yum-arch

profiledir = $(sysconfdir)/profile.d
profile_DATA = bash_completion.sh

bash_completion.sh: bash_completion.sh.in Makefile
	sed -e 's|@sysconfdir[@]|$(sysconfdir)|' <$(srcdir)/$@.in >$@

CLEANFILES = bash_completion.sh

EXTRA_DIST = CHANGES $(sysconf_DATA) $(bashcomp_DATA) bash_completion.sh.in \
	contrib/_mock contrib/_modules contrib/_subversion contrib/_yum \
	contrib/_yum-utils
