%include	/usr/lib/rpm/macros.perl
Summary:	Pod-DocBook perl module
Summary(pl):	Modu³ perla Pod-DocBook
Name:		perl-Pod-DocBook
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Pod/Pod-DocBook-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod-DocBook - module to convert pod files to DocBook SGML.

%description -l pl
Pod-DocBook - modu³ do konwertowania plików pod do formatu DocBook
SGML.

%prep
%setup -q -n Pod-DocBook-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Pod/DocBook
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/pod2docbook

%{perl_sitelib}/Pod/DocBook.pm
%{perl_sitearch}/auto/Pod/DocBook

%{_mandir}/man[13]/*
