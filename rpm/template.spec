Name:           ros-jade-rospilot
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS rospilot package

Group:          Development/Libraries
License:        Apache
Source0:        %{name}-%{version}.tar.gz

Requires:       dnsmasq
Requires:       gdal
Requires:       hostapd
Requires:       libnl3
Requires:       mapnik-python
Requires:       mapnik-utils
Requires:       osm2pgsql
Requires:       postgis
Requires:       python-cherrypy
Requires:       python-colorama
Requires:       python-psutil
Requires:       python-tilestache
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-mavlink
Requires:       ros-jade-message-runtime
Requires:       ros-jade-rosbash
Requires:       ros-jade-rosbridge-suite
Requires:       ros-jade-roslaunch
Requires:       ros-jade-rospy
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-vision-opencv
BuildRequires:  ffmpeg-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libnl3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslint
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs

%description
rospilot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Aug 23 2015 Christopher Berner <christopherberner@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

