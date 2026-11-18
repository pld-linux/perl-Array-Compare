#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Array
%define		pnam	Compare
Summary:	Array::Compare - Perl extension for comparing arrays
Summary(pl.UTF-8):	Array::Compare - rozszerzenie Perla do porównywania tablic
Name:		perl-Array-Compare
Version:	3.0.8
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/D/DA/DAVECROSS/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	5050c871461f0fa370d583088a39fa3c
URL:		http://search.cpan.org/dist/Array-Compare/
BuildRequires:	perl-Module-Build >= 0.42
BuildRequires:	perl-Moo
BuildRequires:	perl-Type-Tiny
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have two arrays and you want to know if they are the same or
different, then Array::Compare Perl module will be useful to you.

%description -l pl.UTF-8
Moduł Perla Array::Compare jest przeznaczony dla posiadaczy dwóch
tablic, którzy chcieliby wiedzieć czy są one identyczne, czy różne.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

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
%{_mandir}/man3/Array::Compare.3pm*
