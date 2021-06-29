Name:           perl-App-s2p
Version:        1.003
Release:        1%{?dist}
Summary:        Convert sed script to Perl program
License:        CC-BY-SA
URL:            https://metacpan.org/release/App-s2p
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-s2p-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(integer)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Devel::FindPerl) >= 0.009
BuildRequires:  perl(File::Copy)
%endif
BuildRequires:  perl(IO::Handle)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Open2)
%endif
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Conflicts:      perl < 4:5.18.2-300

%description
This package delivers s2p tool which converts sed scripts to Perl programs.

%prep
%setup -q -n App-s2p-%{version}
%if %{defined perl_bootstrap}
rm t/s2p.t
sed -i -e '/^t\/s2p\.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Nov 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-1
- 1.003 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-16
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-13
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-8
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-4
- Perl 5.22 re-rebuild of bootstrapped packages

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-3
- Perl 5.22 rebuild

* Thu Jan 08 2015 Petr Pisar <ppisar@redhat.com> - 1.002-2
- Disable a test when bootrapping because of a non-core Devel::FindPerl

* Mon Aug 18 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-1
- 1.002 bump, update license

* Mon Jun 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-1
- Specfile autogenerated by cpanspec 1.78.
