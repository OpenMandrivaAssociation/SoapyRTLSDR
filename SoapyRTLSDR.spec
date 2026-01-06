Name:		SoapyRTLSDR
Version:	0.3.3
Release:	1
Source0:	https://github.com/pothosware/SoapyRTLSDR/archive/soapy-rtl-sdr-%{version}/%{name}-%{version}.tar.gz
Summary:	SoapySDR RTL-SDR Support Module
URL:		https://github.com/pothosware/SoapyRTLSDR
License:	MIT
Group:		Communications/Radio
BuildSystem:	cmake
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(SoapySDR)
BuildRequires:	pkgconfig(librtlsdr)

%description
The Soapy RTL-SDR project provides a plugin module to use the RTL-SDR
dongle within the SoapySDR API and software that supports SoapySDR.

%prep
%autosetup -n SoapyRTLSDR-soapy-rtl-sdr-%{version} -p1

%build
%cmake \
	-DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%post	-p /sbin/ldconfig
%postun	 -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/SoapySDR/modules*/librtlsdrSupport.so
