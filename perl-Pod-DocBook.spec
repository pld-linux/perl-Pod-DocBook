%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	DocBook
Summary:	Pod-DocBook perl module
Summary(pl):	Modu³ perla Pod-DocBook
Name:		perl-Pod-DocBook
Version:	0.05
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod-DocBook - module to convert pod files to DocBook SGML.

%description -l pl
Pod-DocBook - modu³ do konwertowania plików pod do formatu DocBook
SGML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
