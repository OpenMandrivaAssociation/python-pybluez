%define oname PyBluez
%define name python-pybluez
%define version 0.18
%define release %mkrel 1

Summary: Python wrappers around system Bluetooth resources
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pybluez.googlecode.com/files/%{oname}-%{version}.tar.gz
License: GPL
Group: Development/Python
Url: http://org.csail.mit.edu/pybluez/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bluez-devel python-devel

%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/bluetooth/
%{py_platsitedir}/bluetooth/_bluetooth.so
%{py_platsitedir}/bluetooth/*.py*

