
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Array
%define		pnam	Compare
Summary:	Array::Compare perl module
Summary(cs):	Modul Array::Compare pro Perl
Summary(da):	Perlmodul Array::Compare
Summary(de):	Array::Compare Perl Modul
Summary(es):	M�dulo de Perl Array::Compare
Summary(fr):	Module Perl Array::Compare
Summary(it):	Modulo di Perl Array::Compare
Summary(ja):	Array::Compare Perl �⥸�塼��
Summary(ko):	Array::Compare �� ����
Summary(no):	Perlmodul Array::Compare
Summary(pl):	Modu� perla Array::Compare
Summary(pt_BR):	M�dulo Perl Array::Compare
Summary(pt):	M�dulo de Perl Array::Compare
Summary(ru):	������ ��� Perl Array::Compare
Summary(sv):	Array::Compare Perlmodul
Summary(uk):	������ ��� Perl Array::Compare
Summary(zh_CN):	Array::Compare Perl ģ��
Name:		perl-Array-Compare
Version:	1.09
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7830f37c5c26ebd050262771290df734
BuildRequires:	perl-devel >= 5.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::Compare is a Perl module which allows you to compare two arrays.

%description -l pl
Array::Compare jest rozszerzeniem Perla, umo�liwiaj�cym por�wnywanie
dw�ch tablic.

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
