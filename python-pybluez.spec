%define oname pybluez
%define name python-%{oname}
%define version 0.9.2
%define release %mkrel 6

Summary: Python wrappers around system Bluetooth resources
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://org.csail.mit.edu/pybluez/release/%{oname}-src-%{version}.tar.bz2
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
%{py_platsitedir}/_bluetooth.so
%{py_platsitedir}/bluetooth.py*
%{py_platsitedir}/*.egg-info


