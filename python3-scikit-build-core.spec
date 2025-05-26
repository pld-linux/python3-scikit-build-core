Summary:	Build backend for CMake based projects
Name:		python3-scikit-build-core
Version:	0.11.1
Release:	1
License:	Apache v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/scikit-build-core/
Source0:	https://files.pythonhosted.org/packages/source/s/scikit_build_core/scikit_build_core-%{version}.tar.gz
# Source0-md5:	b1d6f9b26e8a9cfc23ee84dfb5ee5759
URL:		https://github.com/scikit-build/scikit-build-core
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scikit-build-core is a build backend for Python that uses CMake to
build extension modules. It has a simple yet powerful static
configuration system in pyproject.toml, and supports almost unlimited
flexibility via CMake. It was initially developed to support the
demanding needs of scientific users, but can build any sort of package
that uses CMake.

%prep
%setup -q -n scikit_build_core-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/scikit_build_core
%{py3_sitescriptdir}/scikit_build_core/*.py
%{py3_sitescriptdir}/scikit_build_core/*.pyi
%{py3_sitescriptdir}/scikit_build_core/__pycache__
%{py3_sitescriptdir}/scikit_build_core/py.typed
%dir %{py3_sitescriptdir}/scikit_build_core/_compat
%{py3_sitescriptdir}/scikit_build_core/_compat/*.py
%{py3_sitescriptdir}/scikit_build_core/_compat/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/_compat/importlib
%{py3_sitescriptdir}/scikit_build_core/_compat/importlib/*.py
%{py3_sitescriptdir}/scikit_build_core/_compat/importlib/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/_vendor
%dir %{py3_sitescriptdir}/scikit_build_core/_vendor/pyproject_metadata
%{py3_sitescriptdir}/scikit_build_core/_vendor/pyproject_metadata/*.py
%{py3_sitescriptdir}/scikit_build_core/_vendor/pyproject_metadata/__pycache__
%{py3_sitescriptdir}/scikit_build_core/_vendor/pyproject_metadata/py.typed
%dir %{py3_sitescriptdir}/scikit_build_core/ast
%{py3_sitescriptdir}/scikit_build_core/ast/*.py
%{py3_sitescriptdir}/scikit_build_core/ast/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/build
%{py3_sitescriptdir}/scikit_build_core/build/*.py
%{py3_sitescriptdir}/scikit_build_core/build/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/builder
%{py3_sitescriptdir}/scikit_build_core/builder/*.py
%{py3_sitescriptdir}/scikit_build_core/builder/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/file_api
%{py3_sitescriptdir}/scikit_build_core/file_api/*.py
%{py3_sitescriptdir}/scikit_build_core/file_api/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/file_api/model
%{py3_sitescriptdir}/scikit_build_core/file_api/model/*.py
%{py3_sitescriptdir}/scikit_build_core/file_api/model/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/hatch
%{py3_sitescriptdir}/scikit_build_core/hatch/*.py
%{py3_sitescriptdir}/scikit_build_core/hatch/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/metadata
%{py3_sitescriptdir}/scikit_build_core/metadata/*.py
%{py3_sitescriptdir}/scikit_build_core/metadata/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/resources
%{py3_sitescriptdir}/scikit_build_core/resources/*.py
%{py3_sitescriptdir}/scikit_build_core/resources/__pycache__
%{py3_sitescriptdir}/scikit_build_core/resources/known_wheels.toml
%{py3_sitescriptdir}/scikit_build_core/resources/scikit-build.schema.json
%dir %{py3_sitescriptdir}/scikit_build_core/resources/find_python
%{py3_sitescriptdir}/scikit_build_core/resources/find_python/*.py
%{py3_sitescriptdir}/scikit_build_core/resources/find_python/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/settings
%{py3_sitescriptdir}/scikit_build_core/settings/*.py
%{py3_sitescriptdir}/scikit_build_core/settings/__pycache__
%dir %{py3_sitescriptdir}/scikit_build_core/setuptools
%{py3_sitescriptdir}/scikit_build_core/setuptools/*.py
%{py3_sitescriptdir}/scikit_build_core/setuptools/__pycache__
%{py3_sitescriptdir}/scikit_build_core-%{version}.dist-info
