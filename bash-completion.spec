Name:		bash-completion
Version:	20040214
Release:	alt01

Summary:	bash-completion offers programmable completion for bash
License:	GPL
Group:		Shells
URL:		http://www.caliban.org/bash/

Source0:	http://www.caliban.org/files/bash/%name-%version.tar.bz2

Requires:	bash >= 2.05
BuildArch:	noarch

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.04 and later.

%prep
%setup -q -n bash_completion

%install
%__install -d %buildroot%_sysconfdir/bash_completion.d
%__install bash_completion %buildroot%_sysconfdir

%__mkdir_p %buildroot%_sysconfdir/profile.d/
%__cat <<__PROFILE__ > %buildroot%_sysconfdir/profile.d/%name.sh
bash=\${BASH_VERSION%.*}; bmajor=\${bash%.*}; bminor=\${bash#*.}
if [ "\$PS1" ] && [ "\$bmajor" -eq 2 ] && [ "\$bminor" '>' 04 ] \\
	&& [ -f %_sysconfdir/bash_completion ]; then	# interactive shell
	# Source completion code
	. %_sysconfdir/bash_completion
fi
unset bash bmajor bminor
__PROFILE__

%files
%doc README Changelog contrib BUGS
%_sysconfdir/bash_completion
%dir %_sysconfdir/bash_completion.d
%attr(0755,root,root) %_sysconfdir/profile.d/%name.sh


%changelog
* Mon Mar 15 2004 Alex Murygin <murygin@altlinux.ru> 20040214-alt01
- new version
- added BUGS to doc

* Thu Jan 08 2004 Alex Murygin <murygin@altlinux.ru> 20040101-alt01
- new version

* Fri Dec 26 2003 Alex Murygin <murygin@altlinux.ru> 20031225-alt01
- new version

* Tue Dec 16 2003 Alex Murygin <murygin@altlinux.ru> 20031215-alt01
- new version

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 20031125-alt01
- First build for Sisyphus.

