#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Pod
%define		pnam	DocBook
Summary:	Pod::DocBook perl module
Summary(pl.UTF-8):	Moduł perla Pod::DocBook
Name:		perl-Pod-DocBook
Version:	1.2
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d3d79d76585025cf8b2af98cee0e519
URL:		http://search.cpan.org/dist/Pod-DocBook/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::DocBook - module to convert pod files to DocBook SGML.

%description -l pl.UTF-8
Pod::DocBook - moduł do konwertowania plików pod do formatu DocBook
SGML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pod2docbook
%{perl_vendorlib}/Pod/DocBook.pm
%{_mandir}/man[13]/*
