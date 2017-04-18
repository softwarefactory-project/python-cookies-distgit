%global pypi_name cookies
%global sum Friendlier RFC 6265-compliant cookie parser/renderer

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        9%{?dist}
Summary:        Friendlier RFC 6265-compliant cookie parser/renderer

License:        MIT
URL:            https://gitlab.com/sashahart/cookies
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:	https://gitlab.com/sashahart/cookies/raw/master/LICENSE

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  pytest



%description
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} .
rm test_cookies.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%check
# removing test_cookies.py to avoid import file mismatch error
# imported module 'test_cookies' has this __file__ attribute:
#   /home/makerpm/rpmbuild/BUILD/cookies-2.2.1/test_cookies.py
# which is not the same as the test file we want to collect:
#   /home/makerpm/rpmbuild/BUILD/cookies-2.2.1/build/lib/test_cookies.py
# Gitlab issue 
# https://gitlab.com/sashahart/cookies/issues/3
#%{__python2} setup.py test
#%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README
%{python2_sitelib}/*

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-8
- Rebuild for Python 3.6

* Sat Oct 29 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.1-7
- Removed remaining and unnecessary python3 conditionals macros

* Wed Oct 26 2016 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-6
- Enable python3 builds for EPEL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-3
- Disabled tests due https://gitlab.com/sashahart/cookies/issues/3

* Fri Jan 22 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-2
- Added data to allow package building on EPEL repository. Only Fedora ships Python3

* Fri Jan 22 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-1
- First commit on Fedora's Git
