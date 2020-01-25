#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Time
%define	pnam	Clock
Summary:	Time::Clock - Twenty-four hour clock object with nanosecond precision.
#Summary(pl.UTF-8):	
Name:		perl-Time-Clock
Version:	1.02
Release:	1
# same as perl (REMOVE THIS LINE IF NOT TRUE)
#License:	GPL v1+ or Artistic
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6a5c938edd37f5e4da35454cec6eae3b
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/Time-Clock/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Time::Clock object is a twenty-four hour clock with nanosecond precision and
wrap-around. It is a clock only; it has absolutely no concept of dates.
Vagaries of date/time such as leap seconds and daylight savings time are
unsupported. Time::Clock objects automatically stringify to a user-definable
format.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*
