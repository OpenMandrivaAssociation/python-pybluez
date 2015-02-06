%define oname PyBluez

Summary: Python wrappers around system Bluetooth resources
Name:    python-pybluez
Version: 0.18
Release: 5
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
