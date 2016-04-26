Name:           nano
Version:        2.3.1
Release:        1
Summary:        Pico Editor Clone with Enhancements

License:        GPL-3.0+
Url:            http://www.nano-editor.org/
Group:          Productivity/Editors/Other
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	nano.manifest
Source1002:     nano.changes

BuildRequires:  file-devel
BuildRequires:  pkgconfig(ncurses)

%description
GNU nano is a small and friendly text editor. It aims to emulate the
Pico text editor while also offering a few enhancements.


%prep
%setup -q
cp %{SOURCE1001} .

# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/nano.c
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/nano.c

%build
%configure --disable-rpath --enable-utf8
make %{?_smp_mflags}

%install
%make_install

# Remove doc files from /usr/share/nano (they should be in defaultdocdir)
rm -rf %{buildroot}%{_datadir}/nano/man-html/
rm -rf %{buildroot}%{_mandir}/fr

%find_lang %{name} --all-name

%docs_package

%lang_package

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_bindir}/nano
%{_bindir}/rnano
%{_datadir}/nano/


%changelog
