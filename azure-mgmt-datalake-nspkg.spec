#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-datalake-nspkg
Version  : 3.0.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/8e/0c/7b705f7c4a41bfeb0b6f3557f227c71aa3fa71555ed76ae934aa7db4b13e/azure-mgmt-datalake-nspkg-3.0.1.zip
Source0  : https://files.pythonhosted.org/packages/8e/0c/7b705f7c4a41bfeb0b6f3557f227c71aa3fa71555ed76ae934aa7db4b13e/azure-mgmt-datalake-nspkg-3.0.1.zip
Summary  : Microsoft Azure Data Lake Management Namespace Package [Internal]
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-datalake-nspkg-python = %{version}-%{release}
Requires: azure-mgmt-datalake-nspkg-python3 = %{version}-%{release}
Requires: azure-mgmt-nspkg
BuildRequires : azure-mgmt-nspkg
BuildRequires : buildreq-distutils3

%description
==============================
        
        This is the Microsoft Azure Data Lake Management namespace package.
        
        This package is not intended to be installed directly by the end user.

%package python
Summary: python components for the azure-mgmt-datalake-nspkg package.
Group: Default
Requires: azure-mgmt-datalake-nspkg-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-datalake-nspkg package.


%package python3
Summary: python3 components for the azure-mgmt-datalake-nspkg package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_datalake_nspkg)
Requires: pypi(azure_mgmt_nspkg)

%description python3
python3 components for the azure-mgmt-datalake-nspkg package.


%prep
%setup -q -n azure-mgmt-datalake-nspkg-3.0.1
cd %{_builddir}/azure-mgmt-datalake-nspkg-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588883347
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
