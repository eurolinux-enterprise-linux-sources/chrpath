Summary: Modify rpath of compiled programs
Name: chrpath
Version: 0.13
Release: 14%{?dist}
License: GPL+
Group: Development/Tools
URL: ftp://ftp.hungry.com/pub/hungry/chrpath/
Source0: ftp://ftp.hungry.com/pub/hungry/chrpath/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Patch0: chrpath-0.13-NULL-entry.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=868611
Patch1: chrpath-0.13-getopt_long.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=925224
Patch2: chrpath-0.13-aarch64.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=948858
Patch3: chrpath-0.13-help.patch

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q
%patch0 -p1 -b .NULL
%patch1 -p1 -b .getopt_long
%patch2 -p1 -b .aarch64
%patch3 -p1 -b .help

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -fr %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS ChangeLog*
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.13-14
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.13-13
- Mass rebuild 2013-12-27

* Mon Apr  8 2013 Petr Machata <pmachata@redhat.com> - 0.13-12
- Add missing help for -k|--keepgoing option
  (chrpath-0.13-help.patch)

* Thu Apr  4 2013 Petr Machata <pmachata@redhat.com> - 0.13-11
- Add missing last entry in long options array
  (chrpath-0.13-getopt_long.patch)
- Update config.sub and config.guess to support aarch64
  (chrpath-0.13-aarch64.patch)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-5
- Fix last entry in .dynamic (by Christian Krause <chkr@plauener.de>).

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.13-2
- License: GPL+

* Sun Mar 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-1
- Initial build.

