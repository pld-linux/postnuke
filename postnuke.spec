# TODO:
# - SECURITY: http://securitytracker.com/alerts/2004/Jul/1010755.html
# - SECURITY: http://securitytracker.com/alerts/2004/Jul/1010733.html
# - SECURITY: http://securitytracker.com/alerts/2004/Apr/1009801.html
# - SECURITY: http://securitytracker.com/alerts/2004/Sep/1011203.html
Summary:	weblog/Content Management System (CMS)
Summary(pl):	System zarz±dzania tre¶ci±
Name:		postnuke
Version:	0.7.2.3
Release:	3
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://developers.postnuke.com/downloads/pn-7.2.3/%{name}-phoenix-%{version}.tar.gz
# Source0-md5:	7b4e49d1724c8e28f9fc2afa381d41e5
# ContentExpress
%define		_ceversion	1.2.6.0
Source1:	http://dl.sourceforge.net/xexpress/ce-%{_ceversion}.zip
# Source1-md5:	bfc7e8de2a993da273099177e2b9ca3f
# Polish lang pack
Source2:	pn-%{version}-pl.tar.gz
# Source2-md5:	dfc1b697125b0e42c65bfff7ff5ddeab
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
PostNuke jest systemem zarz±dzania tre¶ci±. Jest du¿o bardziej
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

%package install
Summary:	weblog/Content Management System (CMS) - installer
Summary(pl):	System zarz±dzania tre¶ci± - instalator
Group:		Applications/Databases/Interfaces
Requires:	%{name} = %{version}

%description install
Package needed to install postnuke.

%description install -l pl
Pakiet potrzebny do zainstalowania postnuke.

%prep
%setup -q -n %{name}-phoenix-%{version} -a1 -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nukeroot}

cp -ar html/		$RPM_BUILD_ROOT%{nukeroot}
cp -ar html/includes/	$RPM_BUILD_ROOT%{nukeroot}
cp -ar modules/		$RPM_BUILD_ROOT%{nukeroot}
install html/index.php	$RPM_BUILD_ROOT%{nukeroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post install
echo "Remember to uninstall %{name}-install after initiation of %{name}!!"

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS.txt INSTALL.txt phoenix-sql/*
%dir %{nukeroot}
%dir %{nukeroot}/html
%attr(640,http,http) %config(noreplace) %{nukeroot}/html/config*.php
%{nukeroot}/html/[^ci]*
%{nukeroot}/html/images
%{nukeroot}/html/includes
%{nukeroot}/includes
%{nukeroot}/modules
%{nukeroot}/html/index.php
%{nukeroot}/index.php

%files install
%defattr(644,root,root,755)
%dir %{nukeroot}/html/install
%attr(640,http,http) %{nukeroot}/html/install/*
%attr(640,http,http) %{nukeroot}/html/install.php
