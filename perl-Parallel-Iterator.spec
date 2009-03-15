
%define realname   Parallel-Iterator
%define version    1.00
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Simple parallel execution
Source:     http://www.cpan.org/modules/by-module/Parallel/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Config)

BuildArch: noarch

%description
The 'map' function applies a user supplied transformation function to each
element in a list, returning a new list containing the transformed
elements.

This module provides a 'parallel map'. Multiple worker processes are forked
so that many instances of the transformation function may be executed
simultaneously.

For time consuming operations, particularly operations that spend most of
their time waiting for I/O, this is a big performance win. It also provides
a simple idiom to make effective use of multi CPU systems.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


