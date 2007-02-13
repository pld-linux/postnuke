# TODO
# - put pl language pack into separate package, such overwriting of
#   the original files is discriminating:)
#   conflicting files list:
#   $ tar tvf ../../../SOURCES/pn-0.760-pl.tar.gz |grep -v /pol/|grep -v '/$'
#   html/docs/COPYING.txt
#   html/includes/pnAPI.php
#   html/includes/templates/dbconnectionerror.htm
#   html/includes/templates/index.html
#   html/includes/templates/siteoff.htm
#   html/install/modify_config.php
#   html/install/newdata.php
#   html/install/upgrade.php
#   html/language/languages.php
#   html/modules/index.html
# - contentexpress module is not installed
# - use system Smarty and adodb
# - %%lang for install/lang/pol,fra,... messages?
Summary:	weblog/Content Management System (CMS)
Summary(pl.UTF-8):	System zarządzania treścią
Name:		postnuke
Version:	0.762
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://downloads.postnuke.com/sf/postnuke/PostNuke-%{version}.tar.gz
# Source0-md5:	ea25bb933c4a99b30854815215dcdbb6
# ContentExpress
%define		_ceversion	1.2.7.5
Source1:	http://dl.sourceforge.net/xexpress/ce-%{_ceversion}.tar.gz
# Source1-md5:	94840261251bbfa5b4b113d0f3c7faef
# Polish lang hpack
Source2:	pn-0.760-pl.tar.gz
# Source2-md5:	635f46d8a622a6cbff23da18ef19c95d
Source3:	%{name}-apache.conf
Patch0:		%{name}-pnTemp.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-smarty.patch
URL:		http://www.postnuke.com/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	Smarty >= 2.6.10-4
Requires:	php(exif)
Requires:	php(mysql)
Requires:	php(tokenizer)
Requires:	php-common >= 3:4.0.2
Requires:	webapps
Obsoletes:	postnuke-install
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
%define		_smartyplugindir	/usr/share/php/Smarty/plugins

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

%description -l pl.UTF-8
PostNuke jest systemem zarządzania treścią. Jest dużo bardziej
bezpieczny i stabilny niż konkurencyjne produkty i może z łatwością
działać w środowiskach z dużym ruchem.

Niektóre zalety PostNuke to:
- konfigurowalność wszystkich aspektów wyglądu serwisu WWW poprzez
  motywy, wraz z obsługą CSS
- możliwość określenia elementów jako odpowiednich dla jednego lub
  wszystkich języków
- najlepsza gwarancja wyświetlania stron we wszystkich przeglądarkach
  dzięki zgodności ze standardem HTML 4.01 transitional
- standardowe API i obszerna dokumentacja, pozwalające na łatwe
  tworzenie dodatkowej funkcjonalności poprzez moduły i bloki.

Ten pakiet zawiera dodatkowe moduły:
- ContentExpress-%{_ceversion}

%package setup
Summary:	Postnuke setup package
Summary(pl.UTF-8):	Pakiet do wstępnej konfiguracji Postnuke
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial Postnuke installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl.UTF-8
Ten pakiet należy zainstalować w celu wstępnej konfiguracji Postnuke
po pierwszej instalacji. Potem należy go odinstalować, jako że
pozostawienie plików instalacyjnych mogłoby być niebezpieczne.

%prep
%setup -q -n PostNuke-%{version} -a1 -a2
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'
%patch0 -p1
%patch1 -p1
%patch2 -p1

> html/config-old.php

install -d smarty
mv html/includes/classes/Smarty/plugins/resource.{userdb,var}.php smarty
rm -rf html/includes/classes/Smarty

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},/var/lib/postnuke,%{_smartyplugindir}}
cp -a html/* $RPM_BUILD_ROOT%{_appdir}
mv $RPM_BUILD_ROOT%{_appdir}/config.php $RPM_BUILD_ROOT%{_sysconfdir}
mv $RPM_BUILD_ROOT%{_appdir}/config-old.php $RPM_BUILD_ROOT%{_sysconfdir}
mv $RPM_BUILD_ROOT%{_appdir}/pnTemp $RPM_BUILD_ROOT/var/lib/postnuke

install -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -p smarty/* $RPM_BUILD_ROOT%{_smartyplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post setup
chmod 660 %{_sysconfdir}/config.php
chown root:http %{_sysconfdir}/config.php

%postun setup
if [ "$1" = "0" ]; then
	chmod 640 %{_sysconfdir}/config.php
	chown root:http %{_sysconfdir}/config.php
fi

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- %{name} < 0.762-1.7
if [ -f /home/services/httpd/html/postnuke/config.php.rpmsave ]; then
	mv -f %{_sysconfdir}/config.php{,.rpmnew}
	mv -f /home/services/httpd/html/postnuke/config.php.rpmsave %{_sysconfdir}/config.php
fi

# no earlier registration, just register with apache2
if [ -d /etc/httpd/webapps.d ]; then
	/usr/sbin/webapp register httpd %{_webapp}
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)
%doc phoenix-sql/*
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%dir %{_appdir}
%{_appdir}/docs
%{_appdir}/images
%{_appdir}/includes
%{_appdir}/javascript
%{_appdir}/language
%{_appdir}/modules
%{_appdir}/themes
%{_appdir}/*.php
%{_appdir}/*.txt
%exclude %{_appdir}/install.php
%{_smartyplugindir}/*

%defattr(644,http,http,755)
/var/lib/postnuke

%files setup
%defattr(644,root,root,755)
%defattr(644,http,http,755)
%{_appdir}/install
%{_appdir}/install.php
