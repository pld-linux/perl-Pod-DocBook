%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	DocBook
Summary:	Pod::DocBook perl module
Summary(pl):	Modu� perla Pod::DocBook
Name:		perl-Pod-DocBook
Version:	0.05
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::DocBook - module to convert pod files to DocBook SGML.

%description -l pl
Pod::DocBook - modu� do konwertowania plik�w pod do formatu DocBook
SGML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/pod2docbook
%{perl_vendorlib}/Pod/DocBook.pm
%{_mandir}/man[13]/*