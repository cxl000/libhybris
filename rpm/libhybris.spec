Name:      libhybris
Version:   0.0.0
Release:   1%{?dist}
Summary:   Hybris allowing us to use bionic-based HW adaptations in glibc systems

Group:	   System
License:   Apache 2.0
URL:	   https://github.com/libhybris/libhybris
Source0:   %{name}-%{version}.tar.bz2
BuildRequires: libtool
# Needed for --enable-wayland
BuildRequires: pkgconfig(wayland-client)

%description
%{summary}.

%package devel
Summary: Common development headers for libhybris
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package libEGL
Summary: EGL for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libEGL
Provides: libEGL.so.1

%description libEGL
%{summary}.

%package libEGL-devel
Summary: EGL development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libEGL-devel

%description libEGL-devel
%{summary}.

%package libGLESv1
Summary: GLESv1 for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv1
Provides: libGLES_CM.so.1

%description libGLESv1
%{summary}.

%package libGLESv1-devel
Summary: GLESv1 development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv1 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv1-devel

%description libGLESv1-devel
%{summary}.

%package libGLESv2
Summary: GLESv2 for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLESv2
Provides: libGLESv2.so.2

%description libGLESv2
%{summary}.

%package libGLESv2-devel
Summary: GLESv2 development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libGLESv2-devel

%description libGLESv2-devel
%{summary}.

%package libOpenCL
Summary: OpenCL for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenCL

%description libOpenCL
%{summary}.

%package libOpenCL-devel
Summary: OpenVG development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenCL = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenCL-devel

%description libOpenCL-devel
%{summary}.

%package libOpenVG
Summary: OpenVG for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOpenVG

%description libOpenVG
%{summary}.

%package libOpenVG-devel
Summary: OpenVG development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libOpenVG = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Provides: libOpenVG-devel

%description libOpenVG-devel
%{summary}.

%package libwayland-egl
Summary: Wayland EGL for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}
Provides: libwayland-egl

%description libwayland-egl
%{summary}.

%package libwayland-egl-devel
Summary: Wayland EGL development headers for hybris
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libwayland-egl = %{version}-%{release}
Provides: libwayland-egl-devel

%description libwayland-egl-devel
%{summary}.

%package libhardware
Summary: The libhardware wrapping of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libhardware
%{summary}.

%package libhardware-devel
Summary: The development headers of libhardware wrapping of libhybris
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}

%description libhardware-devel
%{summary}.

%package libui
Summary: The libui of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libui
%{summary}.

%package libui-devel
Summary: The development files for libui of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libui = %{version}-%{release}

%description libui-devel
%{summary}.

%package libsf
Summary: The libsf of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libsf
%{summary}.

%package libsf-devel
Summary: The development files for libsf of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libsf = %{version}-%{release}

%description libsf-devel
%{summary}.

%package libcamera
Summary: The libcamera of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libcamera
%{summary}.

%package libcamera-devel
Summary: The development files for libcamera of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libcamera = %{version}-%{release}

%description libcamera-devel
%{summary}.

%package libis
Summary: The libis of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libis
%{summary}.

%package libis-devel
Summary: The development files for libis of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libis = %{version}-%{release}

%description libis-devel
%{summary}.

%package libsync
Summary: The libsync of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}

%description libsync
%{summary}.

%package libsync-devel
Summary: The development files for libsync of libhybris
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}

%description libsync-devel
%{summary}.

%package tests
Summary: Tests for %{name}
Group:   System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libEGL = %{version}-%{release}
Requires: %{name}-libGLESv2 = %{version}-%{release}
Requires: %{name}-libcamera = %{version}-%{release}
Requires: %{name}-libhardware = %{version}-%{release}
Requires: %{name}-libis = %{version}-%{release}
Requires: %{name}-libsf = %{version}-%{release}
Requires: %{name}-libui = %{version}-%{release}
Requires: %{name}-libsync = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
cd libhybris/hybris
autoreconf -v -f -i
%configure \
  --enable-wayland \
%ifarch %{arm}
  --enable-arch=arm \
%endif
%ifarch %{ix86}
  --enable-arch=x86 \
%endif
%{nil}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd libhybris/hybris
make install DESTDIR=$RPM_BUILD_ROOT

# Remove the static libraries.
rm %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/libhybris/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig
%postun libEGL -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig
%postun libGLESv2 -p /sbin/ldconfig

%post libwayland-egl -p /sbin/ldconfig
%postun libwayland-egl -p /sbin/ldconfig

%post libhardware -p /sbin/ldconfig
%postun libhardware -p /sbin/ldconfig

%post libui -p /sbin/ldconfig
%postun libui -p /sbin/ldconfig

%post libsf -p /sbin/ldconfig
%postun libsf -p /sbin/ldconfig

%post libcamera -p /sbin/ldconfig
%postun libcamera -p /sbin/ldconfig

%post libis -p /sbin/ldconfig
%postun libis -p /sbin/ldconfig

%post libsync -p /sbin/ldconfig
%postun libsync -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc libhybris/hybris/AUTHORS libhybris/hybris/COPYING
%{_libdir}/libhybris-common.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/android/cutils/*.h
%{_includedir}/android/linux/*.h
%{_includedir}/android/system/*.h
%{_includedir}/android/sync/*.h
%{_includedir}/android/version.h
%{_includedir}/hybris/input/*.h
%{_includedir}/hybris/surface_flinger/*.h
%{_libdir}/libhybris-common.so

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*
%{_libdir}/libhybris-eglplatformcommon.so.*
%{_libdir}/libhybris/eglplatform_fbdev.so
%{_libdir}/libhybris/eglplatform_null.so

%files libEGL-devel
%defattr(-,root,root,-)
%{_includedir}/KHR/*.h
%{_includedir}/EGL/*.h
%{_includedir}/hybris/eglplatformcommon/*.h
%{_libdir}/libEGL.so
%{_libdir}/libhybris-eglplatformcommon.so
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/hybris-egl-platform.pc

%files libGLESv1
%defattr(-,root,root,-)
# We don't have implementation of GLESv1 atm.

%files libGLESv1-devel
%defattr(-,root,root,-)
%{_includedir}/GLES/*.h

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.2*

%files libGLESv2-devel
%defattr(-,root,root,-)
%{_includedir}/GLES2/*.h
%{_libdir}/libGLESv2.so
%{_libdir}/pkgconfig/glesv2.pc

%files libOpenCL
%defattr(-,root,root,-)
# We don't have implementation of OpenCL atm.

%files libOpenCL-devel
%defattr(-,root,root,-)
%{_includedir}/CL/*.h
%{_includedir}/CL/*.hpp

%files libOpenVG
%defattr(-,root,root,-)
# We don't have implementation of OpenVG atm.

%files libOpenVG-devel
%defattr(-,root,root,-)
%{_includedir}/VG/*.h

%files libwayland-egl
%defattr(-,root,root,-)
%{_libdir}/libhybris/eglplatform_wayland.so
%{_libdir}/libwayland-egl.so.*

%files libwayland-egl-devel
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc

%files libhardware
%defattr(-,root,root,-)
%{_libdir}/libhardware.so.*

%files libhardware-devel
%defattr(-,root,root,-)
%{_libdir}/libhardware.so
%{_includedir}/android/hardware/*.h

%files libui
%defattr(-,root,root,-)
%{_libdir}/libui.so.*

%files libui-devel
%defattr(-,root,root,-)
%{_libdir}/libui.so
%{_includedir}/hybris/ui/ui_compatibility_layer.h

%files libsf
%defattr(-,root,root,-)
%{_libdir}/libsf.so.*

%files libsf-devel
%defattr(-,root,root,-)
%{_libdir}/libsf.so

%files libcamera
%defattr(-,root,root,-)
%{_libdir}/libcamera.so.*

%files libcamera-devel
%defattr(-,root,root,-)
%{_libdir}/libcamera.so
%{_includedir}/hybris/camera/*.h

%files libis
%defattr(-,root,root,-)
%{_libdir}/libis.so.*

%files libis-devel
%defattr(-,root,root,-)
%{_libdir}/libis.so

%files libsync
%defattr(-,root,root,-)
%{_libdir}/libsync.so.*

%files libsync-devel
%defattr(-,root,root,-)
%{_libdir}/libsync.so

%files tests
%defattr(-,root,root,-)
%{_bindir}/test_*

