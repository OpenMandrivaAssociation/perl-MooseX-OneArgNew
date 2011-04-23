%define upstream_name    MooseX-OneArgNew
%define upstream_version 0.001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Teach ->new to accept single, non-hashref arguments
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(Test::More) >= 0.960
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


