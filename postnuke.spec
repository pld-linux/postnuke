Summary:	weblog/Content Management System (CMS)
Summary(pl):	System zarz±dzania zawarto¶ci±
Name:		postnuke
Version:	0.7.2.1
Release:	3
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://www.postnuke.com/downloads/pn-%{version}_phoenix.tgz
# Should be removed in next release
# Original from: http://www.postnuke.com/downloads/pnsecuritypatch-002h.zip
Source1:	%{name}-index.php
Source2:	%{name}-pnAPI.php
# ContentExpress
%define		_ceversion	1.2.4.1
Source3:	ce-%{_ceversion}.zip
URL:		http://www.postnuke.com/
Requires:	php-exif
Requires:	php-mysql >= 4.0.2
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		nukeroot	/home/services/httpd/html/postnuke

%description
PostNuke is a weblog/Content Management System (CMS). It is far more
secure and stable than competing products, and able to work in
high-volume environments with ease.

Some of the highlights of PostNuke are:

- Customisation of all aspects of the website's appearance through
  themes, including CSS support
- The ability to specify items as being suitable for either a single
  or all languages
- The best guarantee of displaying your webpages on all browsers due
  to HTML 4.01 transitional compliance
- A standard API and extensive documentation to allow for easy
  creation of extended functionality through modules and blocks

This package includes additional modules:
- ContentExpress-%{_ceversion}

%description -l pl
PostNuke jest systemem zarz±dzania zawarto¶ci±. Jest du¿o bardziej
bezpieczny i stabilny ni¿ konkurencyjne produkty i mo¿e z ³atwo¶ci±
dzia³aæ w ¶rodowiskach z du¿ym ruchem.

Niektóre zalety PostNuke to:
 - konfigurowalno¶æ wszystkich aspektów wygl±du serwisu WWW poprzez
   motywy, wraz z obs³ug± CSS
 - mo¿liwo¶æ okre¶lenia elementów jako odpowiednich dla jednego lub
   wszystkich jêzyków
 - najlepsza gwarancja wy¶wietlania stron we wszystkich przegl±darkach
   dziêki zgodno¶ci ze standardem HTML 4.01 transitional
 - standardowe API i obszerna dokumentacja, pozwalaj±ce na ³atwe
   tworzenie dodatkowej funkcjonalno¶ci poprzez modu³y i bloki.
 
Ten pakiet zawiera dodatkowe modu³y:
- ContentExpress-%{_ceversion}

%prep
%setup -q -n pn-%{version}_Phoenix -a3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nukeroot}

install %{SOURCE1} html/modules/Web_Links/index.php
install %{SOURCE2} html/includes/pnAPI.php
cp -ar html/* $RPM_BUILD_ROOT%{nukeroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangLog CREDITS.txt INSTALL.txt phoenix-sql/*
%dir %{nukeroot}
%attr(640,http,http) %config(noreplace) %{nukeroot}/config*.php
%{nukeroot}/[^c]*
