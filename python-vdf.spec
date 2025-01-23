%global pypi_name vdf

Name:       python-%{pypi_name}
Version:    3.4
Release:    1
Summary:    Package for working with Valve's text and binary KeyValue format
BuildArch:  noarch
License:    MIT
URL:        https://github.com/ValvePython/vdf
Source0:    Source0:	https://files.pythonhosted.org/packages/source/v/vdf/vdf-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)

BuildSystem:	python

%description
Pure python module for (de)serialization to and from VDF that works just like json.}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%files 
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}*.egg-info
