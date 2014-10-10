%define upstream_name    MooseX-OneArgNew
%define upstream_version 0.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Teach ->new to accept single, non-hashref arguments
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-OneArgNew-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(Test::More) >= 0.960
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
MooseX::OneArgNew lets your constructor take a single argument, which will
be translated into the value for a one-entry hashref. It is a the
parameterized role|MooseX::Role::Parameterized manpage with two parameters:

* type

  The Moose type that the single argument must be for the one-arg form to
  work. This should be an existing type, and may be either a string type or
  a MooseX::Type.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 685625
- update to new version 0.002

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.1.0-2
+ Revision: 657452
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1
+ Revision: 639070
- import perl-MooseX-OneArgNew


