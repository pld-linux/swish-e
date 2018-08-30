#
# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define		rel	10
%define		snap	2014-09-14
%define		snapver	%(echo %{snap} | tr -d '-')
%include	/usr/lib/rpm/macros.perl
Summary:	Simple Web Indexing System for Humans - Enhanced
Summary(pl.UTF-8):	Prosty system indeksowania stron WWW - wersja rozszerzona
Name:		swish-e
Version:	2.7.0
Release:	0.%{snapver}.%{rel}
License:	GPL/LGPL
Group:		Applications/Text
#Source0:	http://swish-e.org/distribution/%{name}-%{version}.tar.gz
Source0:	http://swish-e.org/swish-daily/%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	c6b918413382ff61eb5e224c8b4c6f7d
Patch0:		format-security.patch
Patch1:		namespace.patch
Patch2:		zlib-clash.patch
URL:		http://swish-e.org/
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRequires:	rpm-perlprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Swish-e is Simple Web Indexing System for Humans - Enhanced.

Swish-e can quickly and easily index directories of files or remote
web sites and search the generated indexes.

Swish-e is extremely fast in both indexing and searching, highly
configurable, and can be seamlessly integrated with existing web sites
to maintain a consistent design. Swish-e can index web pages, but can
just as easily index text files, mailing list archives, or data stored
in a relational database.

Swish-e key features are:
- Emacs/Gnus mail index in cooordination with nnir.el
- Fast - many factors that affect speed, but a search on this server
  that returns a thousand documents takes only a few seconds.
- Flexible - a number of configuration options provide you a high
  degree of control over what is indexed and how.
- Powerful - the AND, OR and NOT operators are supported, words can be
  truncated (using *), and searches can be limited to particular fields
  (META tag fields, TITLEs, etc.)
- Free - nothing, zip, zero.
- It's made for Web sites - In indexing HTML files, SWISH-E can ignore
  data in most tags while giving higher relevance to information in
  header and title tags. Titles are extracted from HTML files and appear
  in the search results. SWISH can automatically search your whole Web
  site for you in one pass, if it's under one directory. You can also
  limit your search to words in HTML titles, comments, emphasized tags,
  and META tags. In addition, 8-bit HTML characters can be indexed,
  converted, and searched.
- It creates portable indexes - Index files consist of only one file,
  so they can be transported around and easily maintained.
- You can fix the source - We encourage people to send in patches and
  suggestions on how to make SWISH-E better. You may want to join the
  SWISH-E Discussion.

%description -l pl.UTF-8
Swish-e jest prostym systemem indeksującym WWW dla ludzi - w wersji
rozszerzonej.

Swish-e może zgrabnie i łatwo indeksować katalogi plików lub zdalne
strony WWW i przeszukiwać wygenerowane indeksy.

Swish-e jest ekstremalnie szybki zarówno w indeksowaniu i
wyszukiwaniu, mocno konfigurowalny, i może być łatwo zintegrowany z
istniejącymi stronami WWW w celu konfiguracji jego wyglądu. Swish-e
może indeksować nie tylko strony WWW, ale także pliki tekstowe,
archiwa list pocztowych lub dane przechowywane w relacyjnych bazach
danych.

Kluczowymi właściwościami swish-a są:
- Zgodne z Emacs/Gnus indeksowanie poczty w połączeniu z nnir.el
- Szybki - wiele współczynników ma wpływ na prędkość, ale wyszukiwanie
  na serwerze zwracające tysiące dokumentów zabiera tylko kilka sekund.
- Elastyczny - duża liczba opcji konfiguracyjnych udostępnia wysoki
  stopień możliwości określenia co i jak ma być indeksowane.
- Potężny - operatory AND, OR i NOT są obsługiwane, słowa mogą być
  obcinane(korzystając z *), i wyszukiwanie ograniczane do konkretnych
  pól (znaczniki META, tytuły itp.)
- Wolny - bezpłatny, darmowy, za friko.
- Stworzony dla stron WWW - indeksuje pliki HTML, może ignorować dane
  w większości znaczników, przyznając większą wagę informacją w
  nagłówkach i tytułach. Tytuły mogą być wyodrębniane z plików HTML i
  pojawiać się w rezultatach wyszukiwania. SWISH może automatycznie
  przeszukać całą stronę WWW w jednym przejściu, jeżeli jest w jednym
  katalogu. Można także ograniczyć wyszukiwanie do słów w tytułach HTML,
  komentarzach i znacznikach META. Dodatkowo - 8-bitowe znaki HTML mogą
  być indeksowane, przekształcane i przeszukiwane.
- Tworzy przenośne indeksy - są zawarte w tylko jednym pliku, więc
  mogą być łatwo transportowane i zarządzane.
- Można poprawić źródła - wszyscy są proszeni o wysyłanie łat i uwag
  jak ulepszyć SWISH-E. Można się też przyłączyć do dyskusji na temat
  SWISH-E.

%package doc
Summary:	Documentation for swish-e
Summary(pl.UTF-8):	Dokumentacja dla swish-e
Group:		Documentation

%description doc
SWISH-E documentation and examples

%description doc -l pl.UTF-8
Dokumentacja i przykłady dla SWISH-E

%package perl
Summary:	SWISH-E - Perl Scripts and Modules
Summary(pl.UTF-8):	SWISH-E - Skrypty i moduły dla Perla
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description perl
Perl SWISH-E language bindings and scripts.

%description perl -l pl.UTF-8
Skrypty i moduły perlowe dla SWISH-E.

%package devel
Summary:	Header files for swish-e
Summary(pl.UTF-8):	Pliki nagłówkowe dla swish-e
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for swish-e.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla swish-e.

%package static
Summary:	Static library for swish-e
Summary(pl.UTF-8):	Biblioteka statyczna dla swish-e
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for swish-e.

%description static -l pl.UTF-8
Biblioteka statyczna dla swish-e.

%prep
%setup -q -n %{name}-%{version}-%{snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--with-pcre
%{__make}
%{?with_tests:%{__make} test}

cd perl
echo skip | \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	CCFLAGS="%{rpmcflags} -I../src" \
	LIBS="%{rpmldflags} -L../src/.libs -lswish-e" \
	SWISHINC=../src \
	SWISHLIBS=-L../src/.libs \
	SWISHVERSION=%{version} \
	SWISHBINDIR=../src

%{__make}
%{?with_tests:%{__make} test}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/%{name} %{name}-doc

%{__make} -C perl install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libswish-e.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswish-e.so.2
%dir %{_prefix}/lib/swish-e
%{_mandir}/man?/*

%files doc
%defattr(644,root,root,755)
%doc %{name}-doc/*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/swish-filter-test
%{_prefix}/lib/%{name}/perl
%attr(755,root,root) %{_prefix}/lib/%{name}/*.pl
%attr(755,root,root) %{_prefix}/lib/%{name}/*.cgi
%{_datadir}/swish-e
%dir %{perl_vendorarch}/SWISH
%{perl_vendorarch}/SWISH/*.pm
%dir %{perl_vendorarch}/auto/SWISH
%dir %{perl_vendorarch}/auto/SWISH/API
%attr(755,root,root) %{perl_vendorarch}/auto/SWISH/API/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/swish-config
%attr(755,root,root) %{_libdir}/libswish-e.so
%{_libdir}/libswish-e.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libswish-e.a
