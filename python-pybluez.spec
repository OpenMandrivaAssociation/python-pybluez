%define oname PyBluez

Summary: Python wrappers around system Bluetooth resources
Name:    python-pybluez
Version: 0.18
Release: 4
Source0: http://pybluez.googlecode.com/files/%{oname}-%{version}.tar.gz
License: GPL
Group: Development/Python
Url: http://org.csail.mit.edu/pybluez/
BuildRequires: pkgconfig(bluez)
BuildRequires: python-devel

%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc CHANGELOG README
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/bluetooth/
#%{py_platsitedir}/bluetooth/_bluetooth.so
#%{py_platsitedir}/bluetooth/*.py*



%changelog
* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.18-3mdv2011.0
+ Revision: 590596
- rebuild for python 2.7

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 0.18-2mdv2010.1
+ Revision: 486803
- rebuild
- Update to new version 0.18
- Update URL

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2-6mdv2010.0
+ Revision: 442411
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.9.2-5mdv2009.1
+ Revision: 320162
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2-4mdv2009.0
+ Revision: 259770
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2-3mdv2009.0
+ Revision: 247596
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.2-1mdv2008.1
+ Revision: 136456
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 0.9.2-1mdv2007.0
+ Revision: 102576
- buildrequires bluez-devel
- buildrequires python-devel
- initial pybluez release
- Create python-pybluez

