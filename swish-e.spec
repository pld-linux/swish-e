%include	/usr/lib/rpm/macros.perl
Summary:	Simple Web Indexing System for Humans - Enhanced
Summary(pl):	Prosty system indeksowania stron WWW - wersja rozszerzona
Name:		swish-e
Version:	2.4.2
Release:	4.1
License:	GPL/LGPL
Group:		Applications/Text
Source0:	http://swish-e.org/Download/%{name}-%{version}.tar.gz
# Source0-md5:	1606e2f55034540f88c1748eeaae5274
URL:		http://swish-e.org/
#Icon:		swish-e.xpm
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

%description -l pl
Swish-e jest prostym systemem indeksuj�cym WWW dla ludzi - w wersji
rozszerzonej.

Swish-e mo�e zgrabnie i �atwo indeksowa� katalogi plik�w lub zdalne
strony WWW i przeszukiwa� wygenerowane indeksy.

Swish-e jest ekstremalnie szybki zar�wno w indeksowaniu i
wyszukiwaniu, mocno konfigurowalny, i mo�e by� �atwo zintegrowany z
istniej�cymi stronami WWW w celu konfiguracji jego wygl�du. Swish-e
mo�e indeksowa� nie tylko strony WWW, ale tak�e pliki tekstowe,
archiwa list pocztowych lub dane przechowywane w relacyjnych bazach
danych.

Kluczowymi w�a�ciwo�ciami swish-a s�:
- Zgodne z Emacs/Gnus indeksowanie poczty w po��czeniu z nnir.el
- Szybki - wiele wsp�czynnik�w ma wp�yw na pr�dko��, ale wyszukiwanie
  na serwerze zwracaj�ce tysi�ce dokument�w zabiera tylko kilka sekund.
- Elastyczny - du�a liczba opcji konfiguracyjnych udost�pnia wysoki
  stopie� mo�liwo�ci okre�lenia co i jak ma by� indeksowane.
- Pot�ny - operatory AND, OR i NOT s� obs�ugiwane, s�owa mog� by�
  obcinane(korzystaj�c z *), i wyszukiwanie ograniczane do konkretnych
  p�l (znaczniki META, tytu�y itp.)
- Wolny - bezp�atny, darmowy, za friko.
- Stworzony dla stron WWW - indeksuje pliki HTML, mo�e ignorowa� dane
  w wi�kszo�ci znacznik�w, przyznaj�c wi�ksz� wag� informacj� w
  nag��wkach i tytu�ach. Tytu�y mog� by� wyodr�bniane z plik�w HTML i
  pojawia� si� w rezultatach wyszukiwania. SWISH mo�e automatycznie
  przeszuka� ca�� stron� WWW w jednym przej�ciu, je�eli jest w jednym
  katalogu. Mo�na tak�e ograniczy� wyszukiwanie do s��w w tytu�ach HTML,
  komentarzach i znacznikach META. Dodatkowo - 8-bitowe znaki HTML mog�
  by� indeksowane, przekszta�cane i przeszukiwane.
- Tworzy przeno�ne indeksy - s� zawarte w tylko jednym pliku, wi�c
  mog� by� �atwo transportowane i zarz�dzane.
- Mo�na poprawi� �r�d�a - wszyscy s� proszeni o wysy�anie �at i uwag
  jak ulepszy� SWISH-E. Mo�na si� te� przy��czy� do dyskusji na temat
  SWISH-E.

%package doc
Summary:	Documentation for swish-e
Summary(pl):	Dokumentacja dla swish-e
Group:		Documentation

%description doc
SWISH-E documentation and examples

%description doc -l pl
Dokumentacja i przyk�ady dla SWISH-E

%package   perl
Summary:	SWISH-E - PERL Scripts and Modules
Summary(pl):	SWISH-E - Skrypty i modu�y dla PERL-a
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description    perl
PERL SWISH-E language bindings and scripts.

%description    perl  -l pl
Skrypty i modu�y perlowe dla SWISH-E.

%package devel
Summary:	Header files for swish-e
Summary(pl):	Pliki nag��wkowe dla swish-e
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for swish-e.

%description devel -l pl
Pliki nag��wkowe dla swish-e.

%package static
Summary:	Static library for swish-e
Summary(pl):	Biblioteka statyczna dla swish-e
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for swish-e.

%description static -l pl
Biblioteka statyczna dla swish-e.

%prep
%setup -q

%build
%configure \
	--with-pcre
%{__make}
%{__make} test

cd perl
echo | \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	CCFLAGS="%{rpmcflags} -I../src" \
	LIBS="%{rpmldflags} -L../src/.libs -lswish-e"

%{__make}
%{__make} test
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/%{name} %{name}-doc

cd perl
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libswish-e.so.*.*.*
%dir %{_prefix}/lib/swish-e
%attr(755,root,root) %{_prefix}/lib/swish-e/swishspider
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
%{perl_vendorarch}/auto/SWISH/API/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SWISH/API/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswish-e.so
%{_libdir}/libswish-e.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libswish-e.a
