Summary:	weblog/Content Management System (CMS)
Name:		postnuke
Version:	0.7.2.1
Release:	2
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://www.postnuke.com/downloads/pn-%{version}_phoenix.tgz
# Should be removed in next release
# Original from: http://www.postnuke.com/downloads/pnsecuritypatch-002h.zip
Source1:	%{name}-index.php
Source2:	%{name}-pnAPI.php
URL:		http://www.postnuke.com/
Requires:	php-exif
Requires:	php-mysql >= 4.0.2
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		nukeroot	/home/httpd/html/postnuke

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

%prep
%setup -q -n pn-%{version}_Phoenix

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
%attr(640,http,http) %config(noreplace) %{nukeroot}/config.php
%{nukeroot}/[^c]*
