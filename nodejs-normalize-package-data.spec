%define		pkg	normalize-package-data
Summary:	Normalizes data that can be found in package.json files
Name:		nodejs-%{pkg}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	1e0cfe6d59f44f5cc0127b089c5d3f82
URL:		https://github.com/meryn/normalize-package-data
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-github-url-from-git < 1.4
Requires:	nodejs-github-url-from-git >= 1.3.0
Requires:	nodejs-github-url-from-username-repo < 1
Requires:	nodejs-github-url-from-username-repo >= 0.2.0
Requires:	nodejs-semver < 4
Requires:	nodejs-semver >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exports a function that normalizes package metadata. This data is
typically found in a package.json file, but in principle could come
from any source - for example the npm registry.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{nodejs_libdir}/%{pkg}
