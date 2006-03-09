Summary:	weblog/Content Management System (CMS)
Summary(pl):	System zarz±dzania tre¶ci±
Name:		postnuke
Version:	0.762
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://downloads.postnuke.com/sf/postnuke/PostNuke-%{version}.tar.gz
# Source0-md5:	ea25bb933c4a99b30854815215dcdbb6
# ContentExpress
%define		_ceversion	1.2.7.5
Source1:	http://dl.sourceforge.net/xexpress/ce-%{_ceversion}.tar.gz
# Source1-md5:	94840261251bbfa5b4b113d0f3c7faef
# Polish lang pack
Source2:	pn-0.760-pl.tar.gz
# Source2-md5:	635f46d8a622a6cbff23da18ef19c95d
URL:		http://www.postnuke.com/
Requires:	php-exif
Requires:	php-mysql >= 3:4.0.2
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
%setup -q -n PostNuke-%{version} -a1 -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nukeroot}

cp -ar html/*		$RPM_BUILD_ROOT%{nukeroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post install
echo "Remember to uninstall %{name}-install after initiation of %{name}!!"

%files
%defattr(644,root,root,755)
%doc phoenix-sql/*
%dir %{nukeroot}
%attr(640,http,http) %config(noreplace) %{nukeroot}/config*.php
%dir %{nukeroot}/pnTemp
%attr(755,http,http) %{nukeroot}/pnTemp/*
%{nukeroot}/[!ip]*
%{nukeroot}/images
%{nukeroot}/includes
%{nukeroot}/index.php
%{nukeroot}/p*.php

%files install
%defattr(644,root,root,755)
%dir %{nukeroot}/install
%attr(750,http,http) %{nukeroot}/install/*
%attr(750,http,http) %{nukeroot}/install.php
