Name:		bash-completion
Version:	20031125
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
%__chmod +x %buildroot%_sysconfdir/profile.d/%name.sh

%files
%doc README Changelog contrib
%_sysconfdir/bash_completion
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/profile.d/%name.sh


%changelog
* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 20031125-alt01
- First build for Sisyphus.

