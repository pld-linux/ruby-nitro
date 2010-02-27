%define pkgname nitro
Summary:	Struts-like web development framework
Summary(pl.UTF-8):	Szkielet do tworzenia WWW podobny do Struts
Name:		ruby-%{pkgname}
Version:	0.27.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/8081/%{pkgname}-%{version}.tgz
# Source0-md5:	2a69ca49a776d066c377136e380312f2
Source1:	http://rubyforge.org/download.php/8092/examples-%{version}.tgz
# Source1-md5:	9593a995f5e53e19b2f0d7c8fe91e8c2
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-glue
Obsoletes:	ruby-Nitro
Provides:	ruby-Nitro
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nitro is a Java Struts-like web development framework, with renderers,
XHTML server pages, and more.

%description -l pl.UTF-8
Nitro to szkielet do tworzenia WWW podobny do Java Struts, z
narzędziami do renderowania, stronami serwerowymi XHTML itd.

%package examples
Summary:	Examples of Nitro's use
Summary(pl.UTF-8):	Przyklady wykorzystania Nitro
Group:		Development/Languages

%description examples
Examples of Nitro's use.

%description examples -l pl.UTF-8
Przyklady wykorzystania Nitro.

%prep
%setup -q -n %{pkgname}-%{version} -a1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_datadir}/%{name},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a src/part $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a proto $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a examples-%{version}/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README CHANGELOG doc/*
%{ruby_rubylibdir}/*
%{_datadir}/%{name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/*
