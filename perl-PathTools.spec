#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PathTools
Summary:	Get pathname of current working directory
Summary(pl):	Pobieranie ¶cie¿ki bie¿±cego katalogu
Name:		perl-PathTools
Version:	3.01
Release:	1
#License:	TODO
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KW/KWILLIAMS/%{pdir}-%{version}.tar.gz
# Source0-md5:	345340b241923ffb0bf1a541e8397855
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
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

%description -l pl
PathTools ³±czy Cwd i File::Spec w jeden pakiet. Zosta³ zrobiony
poniewa¿ te dwa modu³y u¿ywaj± intensywnie siebie nawzajem i
wyci±gniêcie wspólnego kodu do oddzielnego pakietu zosta³o uznane za
prawie niemo¿liwe.

Cwd dostarcza funkcje do okre¶lania ¶cie¿ki bie¿±cego katalogu.
Zalecane jest u¿ywanie getcwd (lub innej funkcji *cwd()) w _ca³ym_
kodzie dla zapewnienia przeno¶no¶ci.

File::Spec jest zaprojektowany do obs³ugi operacji zwykle
przeprowadzanych na okre¶leniach plików (zwykle nazywanych "nazwami
plików", których nie nale¿y myliæ z zawarto¶ci± plików czy perlowymi
uchwytami plików), takich jak ³±czenie kilku katalogów i nazw plików w
pojedyncz± ¶cie¿kê albo okre¶lanie czy ¶cie¿ka jest podana wzglêdem
g³ównego katalogu.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
