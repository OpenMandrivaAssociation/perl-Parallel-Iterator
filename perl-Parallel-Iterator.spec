
%define realname   Parallel-Iterator

Name:		perl-%{realname}
Version:	1.00
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Simple parallel execution
Source:		http://www.cpan.org/modules/by-module/Parallel/%{realname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel
BuildRequires:	perl(Config)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.00-3mdv2011.0
+ Revision: 658543
- rebuild for updated spec-helper

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.00-2mdv2010.0
+ Revision: 375908
- rebuild

* Sun Mar 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.00-1mdv2009.1
+ Revision: 355228
- import perl-Parallel-Iterator


* Sun Mar 15 2009 cpan2dist 1.00-1mdv
- initial mdv release, generated with cpan2dist

