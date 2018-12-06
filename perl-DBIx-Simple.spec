#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-Simple
Version  : 1.37
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/J/JU/JUERD/DBIx-Simple-1.37.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JU/JUERD/DBIx-Simple-1.37.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdbix-simple-perl/libdbix-simple-perl_1.37-1.debian.tar.xz
Summary  : 'Very complete easy-to-use OO interface to DBI'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-DBIx-Simple-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBI)

%description
DBIx::Simple
INSTALLATION
To install this module type the following:
perl Makefile.PL
make
make test
make install

%package dev
Summary: dev components for the perl-DBIx-Simple package.
Group: Development
Provides: perl-DBIx-Simple-devel = %{version}-%{release}

%description dev
dev components for the perl-DBIx-Simple package.


%package license
Summary: license components for the perl-DBIx-Simple package.
Group: Default

%description license
license components for the perl-DBIx-Simple package.


%prep
%setup -q -n DBIx-Simple-1.37
cd ..
%setup -q -T -D -n DBIx-Simple-1.37 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/DBIx-Simple-1.37/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-Simple
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-DBIx-Simple/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/DBIx/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.1/DBIx/Simple/Comparison.pod
/usr/lib/perl5/vendor_perl/5.28.1/DBIx/Simple/Examples.pod
/usr/lib/perl5/vendor_perl/5.28.1/DBIx/Simple/Result/RowObject.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Simple.3
/usr/share/man/man3/DBIx::Simple::Comparison.3
/usr/share/man/man3/DBIx::Simple::Examples.3
/usr/share/man/man3/DBIx::Simple::Result::RowObject.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-Simple/deblicense_copyright
