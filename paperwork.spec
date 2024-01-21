Summary:	A personal document manager
Name:		paperwork
Version:	2.1.2
Release:	1
License:	GPLv3+
URL:		https://www.openpaper.work/en/
Source0:	https://pypi.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	python-%{name} = %{version}-%{release}

BuildArch:	noarch
%description
Paperwork is a personal document manager. It manages scanned documents 
and PDFs.

It's designed to be easy and fast to use. The idea behind Paperwork is
"scan & forget": You can just scan a new document and forget about it
until the day you need it again.

In other words, let the machine do most of the work for you.

This package provides the GTK frontend for paperwork.

%files
%{_bindir}/paperwork-gtk
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml

#----------------------------------------------------------------------

%package -n python-%{name}
Summary:	%{summary}
BuildRequires:	libnotify
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	python%{pyver}dist(openpaperwork-core)
BuildRequires:	python%{pyver}dist(openpaperwork-gtk)
BuildRequires:	python%{pyver}dist(paperwork-backend)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(pycountry)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(pyocr)
BuildRequires:	python%{pyver}dist(python-levenshtein)
BuildRequires:	python%{pyver}dist(pyxdg)

Requires:	tesseract-osd
Requires:	typelib(Libinsane)

%description -n python-%{name}
Paperwork is a personal document manager. It manages scanned documents 
and PDFs.

It's designed to be easy and fast to use. The idea behind Paperwork is
"scan & forget": You can just scan a new document and forget about it
until the day you need it again.

In other words, let the machine do most of the work for you.

%files -n python-%{name}
%doc README.markdown
%{py_sitedir}/paperwork_gtk
%{py_sitedir}/paperwork-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

PYTHONPATH=%{buildroot}%{python_sitelib} \
	xvfb-run -a \
		%{__python} -m paperwork_gtk.main install \
			--data_base_dir %{buildroot}%{_datadir} \
			--icon_base_dir %{buildroot}%{_datadir}/icons

