%define oname PyBluez

Summary: Python wrappers around system Bluetooth resources
Name:    python-pybluez
Version: 0.23
Release: 1
Source0: https://files.pythonhosted.org/packages/08/9f/e9d93b266d2d1ea988780a52a696073ba0a65df65a532165fdf6ff90d0ed/%{oname}-%{version}.tar.gz
License: GPL
Group: Development/Python
Url: https://github.com/pybluez/pybluez
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)

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
