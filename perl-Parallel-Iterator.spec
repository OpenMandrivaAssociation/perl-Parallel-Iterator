%define modname   Parallel-Iterator

Summary:	Simple parallel execution
Name:		perl-%{modname}
Version:	1.00
Release:	6
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Config)

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
%setup -qn %{modname}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

