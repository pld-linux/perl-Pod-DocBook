%include	/usr/lib/rpm/macros.perl
Summary:	Pod-DocBook perl module
Summary(pl):	Modu� perla Pod-DocBook
Name:		perl-Pod-DocBook
Version:	0.05
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Pod/Pod-DocBook-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod-DocBook - module to convert pod files to DocBook SGML.

%description -l pl
Pod-DocBook - modu� do konwertowania plik�w pod do formatu DocBook
SGML.

%prep
%setup -q -n Pod-DocBook-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pod2docbook
%{perl_sitelib}/Pod/DocBook.pm
%{_mandir}/man[13]/*
