Name:           ros-hydro-nao-teleop
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS nao_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nao_remote
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-joy
Requires:       ros-hydro-naoqi-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-naoqi-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs

%description
Teleoperation (gamepad or joystick) for the Nao humanoid

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Nov 13 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Sun Sep 07 2014 Armin Hornung <HornungA@informatik.uni-freiburg.de> - 0.2.1-0
- Autogenerated by Bloom

