#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	Compare
Summary:	Array::Compare - Perl extension for comparing arrays
Summary(pl):	Array::Compare - rozszerzenie Perla do porównywania tablic
Name:		perl-Array-Compare
Version:	1.10
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4604bc5c717b098d2a2f6063a8a336a0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have two arrays and you want to know if they are the same or
different, then Array::Compare Perl module will be useful to you.


%description -l pl
Modu³ Perla Array::Compare jest przeznaczony dla posiadaczy dwóch
tablic, którzy chcieliby wiedzieæ czy s± one identyczne, czy ró¿ne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Array/Compare.pm
%{_mandir}/man3/*.3pm*
