#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PathTools
Summary:	Get pathname of current working directory
Summary(pl.UTF-8):	Pobieranie ścieżki bieżącego katalogu
Name:		perl-PathTools
Version:	3.31
Release:	3
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SM/SMUELLER/%{pdir}-%{version}.tar.gz
# Source0-md5:	48d473cea29f4c14631b3600f820480c
URL:		http://search.cpan.org/dist/PathTools/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PathTools merges Cwd and File::Spec into a single distribution.
This was done because the two modules use each other fairly extensively,
and extracting the common stuff into another distribution was deemed
nigh-impossible.

Cwd provides functions for determining the pathname of the current
working directory.  It is recommended that getcwd (or another *cwd()
function) be used in _all_ code to ensure portability.

File::Spec is designed to support operations commonly performed on file
specifications (usually called "file names", but not to be confused with
the contents of a file, or Perl's file handles), such as concatenating
several directory and file names into a single path, or determining
whether a path is rooted.

%description -l pl.UTF-8
PathTools łączy Cwd i File::Spec w jeden pakiet. Został zrobiony
ponieważ te dwa moduły używają intensywnie siebie nawzajem i
wyciągnięcie wspólnego kodu do oddzielnego pakietu zostało uznane za
prawie niemożliwe.

Cwd dostarcza funkcje do określania ścieżki bieżącego katalogu.
Zalecane jest używanie getcwd (lub innej funkcji *cwd()) w _całym_
kodzie dla zapewnienia przenośności.

File::Spec jest zaprojektowany do obsługi operacji zwykle
przeprowadzanych na określeniach plików (zwykle nazywanych "nazwami
plików", których nie należy mylić z zawartością plików czy perlowymi
uchwytami plików), takich jak łączenie kilku katalogów i nazw plików w
pojedynczą ścieżkę albo określanie czy ścieżka jest podana względem
głównego katalogu.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{perl_vendorarch}/File/Spec/,%{_mandir}/man3/File::Spec::}{Cygwin,Epoc,Mac,OS2,VMS,Win32}*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/File/Spec*
%dir %{perl_vendorarch}/auto/Cwd
%{perl_vendorarch}/auto/Cwd/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Cwd/*.so
%{_mandir}/man3/*
