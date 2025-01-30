Name      : pxn-aliases
Summary   : Helpful aliases for common shell commands.
Version   : 2.2.%{?build_number}%{!?build_number:x}
Release   : 1
BuildArch : noarch
Packager  : PoiXson <support@poixson.com>
License   : AGPLv3+ADD-PXN-V1
URL       : https://poixson.com/

Provides  : pxnaliases

Prefix: %{_bindir}/pxn/scripts
%define _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%global source_date_epoch_from_changelog 0
%define source_date_epoch 0

%description
Helpful aliases for common shell commands.



### Install ###
%install
echo
echo "Install.."

# create dirs
%{__install} -d -m 0755  \
	"%{buildroot}%{_bindir}/"                \
	"%{buildroot}%{prefix}/"                 \
	"%{buildroot}%{_sysconfdir}/profile.d/"  \
		|| exit 1

# scripts
\pushd  "%{_topdir}/../src/"  >/dev/null  || exit 1
	# /usr/bin/pxn/scripts/
	%{__install} -m 0644  \
		"aliases.sh"  \
			"%{buildroot}%{prefix}/"  || exit 1
\popd  >/dev/null

# /etc/profile.d/
\pushd  "%{_topdir}/../src/profile.d/"  >/dev/null  || exit 1
	%{__install} -m 0644  "pxn-aliases.sh"  "%{buildroot}%{_sysconfdir}/profile.d/pxnaliases.sh"  || exit 1
\popd  >/dev/null



### Files ###
%files
%defattr(0555, root, root, 0755)
%dir %{prefix}/
# scripts
%{prefix}/aliases.sh
# profile.d
%{_sysconfdir}/profile.d/pxnaliases.sh
