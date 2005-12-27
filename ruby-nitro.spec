Summary:	Struts-like web development framework
Summary(pl):	Szkielet do tworzenia WWW podobny do Struts
Name:		ruby-Nitro
%define tarname nitro
Version:	0.25.0
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/7158/%{tarname}-%{version}.tgz
# Source0-md5:	604a9676b17edd41f0167637048554e1
Patch0:		%{name}-FHS.patch
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
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
%setup -q -n %{tarname}
%patch0 -p1

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
%{ruby_ridir}/N*
%{ruby_ridir}/*Shader*
%{_datadir}/%{name}
