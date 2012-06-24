#
# Conditional build:
# _without_tests - do not perform "make test"
#
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
Version:	1.03
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Array/Compare.pm
%dir %{perl_sitelib}/auto/Array/Compare
%{perl_sitelib}/auto/Array/Compare/*.ix
%{_mandir}/man3/*.3pm*
