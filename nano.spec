%define name	nano
%define version	2.3.1
%define release	1

Summary	: Pico editor clone with enhancements
Name		: %{name}
Version		: %{version}
Release		: %{release}
License		: GPL
Group		: Applications/Editors
URL		: http://www.nano-editor.org/
Source		: http://www.nano-editor.org/dist/v2.0/%{name}-%{version}.tar.gz
BuildRoot	: %{_tmppath}/%{name}-%{version}-root
BuildRequires	: autoconf, automake, gettext-devel, ncurses-devel

%description
GNU nano is a small and friendly text editor.  It aims to emulate the
Pico text editor while also offering a few enhancements.

%prep
%setup -q

%build
%configure --enable-all
make

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" install

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README THANKS TODO doc/faq.html doc/nanorc.sample
%{_bindir}/*
%{_mandir}/man*/*
%{_mandir}/fr/man*/*
%{_infodir}/nano.info*
%{_datadir}/locale/*/LC_MESSAGES/nano.mo
%{_datadir}/nano/*
