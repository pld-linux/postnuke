Summary:	weblog/Content Management System (CMS)
Summary(pl):	System zarz±dzania tre¶ci±
Name:		postnuke
Version:	0.7.5.0a
Release:	1.1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://downloads.postnuke.com/sf/postnuke/PostNuke-0.750a.tar.gz
# Source0-md5:	dcb276fa0aae4e22764eb22fd66ccd09
# ContentExpress
%define		_ceversion	1.2.7.5
Source1:	http://dl.sourceforge.net/xexpress/ce-%{_ceversion}.tar.gz
# Source1-md5:	94840261251bbfa5b4b113d0f3c7faef
# Polish lang pack
Source2:	pn-0.7.5.0-pl.tar.gz
# Source2-md5:	08e6850526cb8372a1e6b50bc3c1e155
URL:		http://www.postnuke.com/
Requires:	php-exif
Requires:	php-mysql >= 4.0.2
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		nukeroot	/home/services/httpd

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
%setup -q -n PostNuke-0.750 -a1 -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nukeroot}

cp -ar html/		$RPM_BUILD_ROOT%{nukeroot}
cp -ar html/includes/	$RPM_BUILD_ROOT%{nukeroot}
cp -ar html/modules/		$RPM_BUILD_ROOT%{nukeroot}
install html/index.php	$RPM_BUILD_ROOT%{nukeroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post install
echo "Remember to uninstall %{name}-install after initiation of %{name}!!"

%files
%defattr(644,root,root,755)
%doc html/docs/ChangeLog.txt html/docs/CREDITS.txt phoenix-sql/*
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
