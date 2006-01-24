Summary:	Struts-like web development framework
Summary(pl):	Szkielet do tworzenia WWW podobny do Struts
Name:		ruby-Nitro
%define tarname nitro
Version:	0.27.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/8081/%{tarname}-%{version}.tgz
# Source0-md5:	2a69ca49a776d066c377136e380312f2
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-Glue
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nitro is a Java Struts-like web development framework, with renderers,
XHTML server pages, and more.

%description -l pl
Nitro to szkielet do tworzenia WWW podobny do Java Struts, z
narzêdziami do renderowania, stronami serwerowymi XHTML itd.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_datadir}/%{name}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a src/part $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a proto $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README CHANGELOG doc/*
%{ruby_rubylibdir}/*
%{_datadir}/%{name}
