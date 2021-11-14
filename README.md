



# Crash message :

```
[xcb] Unknown sequence number while processing queue
[xcb] Most likely this is a multi-threaded client and XInitThreads has not been called
[xcb] Aborting, sorry about that.
python: ../../src/xcb_io.c:269: poll_for_event: Assertion `!xcb_xlib_threads_sequence_lost' failed.
Aborted
```

# Install python environment :

```
python3 -m venv env
source env/bin/activate
pip install -U pip wheel setuptools
pip install PyGObject
```

# Run script :

```
python main.py
```

# pip freeze :

```
PyGObject==3.42.0
```


# Installed debian x11 packages informations

```
ii  libx11-6:amd64                        2:1.7.2-1                       amd64        X11 client-side library
ii  libx11-6:i386                         2:1.7.2-1                       i386         X11 client-side library
ii  libx11-data                           2:1.7.2-1                       all          X11 client-side library
ii  libx11-dev:amd64                      2:1.7.2-1                       amd64        X11 client-side library (development headers)
ii  libx11-protocol-perl                  0.56-7.1                        all          Perl module for the X Window System Protocol, version 11
ii  libx11-xcb1:amd64                     2:1.7.2-1                       amd64        Xlib/XCB interface library
ii  libx11-xcb1:i386                      2:1.7.2-1                       i386         Xlib/XCB interface library
```

# Installed debian python3 packages informations

```
ii  libpython3-dev:amd64                  3.9.2-3                         amd64        header files and a static library for Python (default)
ii  libpython3-stdlib:amd64               3.9.2-3                         amd64        interactive high-level object-oriented language (default python3 version)
ii  libpython3.9:amd64                    3.9.2-1                         amd64        Shared Python runtime library (version 3.9)
ii  libpython3.9-dbg:amd64                3.9.2-1                         amd64        Debug Build of the Python Interpreter (version 3.9)
ii  libpython3.9-dev:amd64                3.9.2-1                         amd64        Header files and a static library for Python (v3.9)
ii  libpython3.9-minimal:amd64            3.9.2-1                         amd64        Minimal subset of the Python language (version 3.9)
ii  libpython3.9-stdlib:amd64             3.9.2-1                         amd64        Interactive high-level object-oriented language (standard library, version 3.9)
ii  python3                               3.9.2-3                         amd64        interactive high-level object-oriented language (default python3 version)
ii  python3-apt                           2.2.1                           amd64        Python 3 interface to libapt-pkg
ii  python3-brlapi:amd64                  6.3+dfsg-1                      amd64        Braille display access via BRLTTY - Python3 bindings
ii  python3-cairo:amd64                   1.16.2-4+b2                     amd64        Python3 bindings for the Cairo vector graphics library
ii  python3-certifi                       2020.6.20-1                     all          root certificates for validating SSL certs and verifying TLS hosts (python3)
ii  python3-chardet                       4.0.0-1                         all          universal character encoding detector for Python3
ii  python3-cups:amd64                    2.0.1-4+b1                      amd64        Python3 bindings for CUPS
ii  python3-cupshelpers                   1.5.14-1                        all          Python utility modules around the CUPS printing system
ii  python3-dbus                          1.2.16-5                        amd64        simple interprocess messaging system (Python 3 interface)
ii  python3-debconf                       1.5.77                          all          interact with debconf from Python 3
ii  python3-debian                        0.1.39                          all          Python 3 modules to work with Debian-related data formats
ii  python3-debianbts                     3.1.0                           all          Python interface to Debian's Bug Tracking System
ii  python3-dev                           3.9.2-3                         amd64        header files and a static library for Python (default)
ii  python3-distro                        1.5.0-1                         all          Linux OS platform information API
ii  python3-distro-info                   1.0                             all          information about distributions' releases (Python 3 module)
ii  python3-distutils                     3.9.2-1                         all          distutils package for Python 3.x
ii  python3-gi                            3.38.0-2                        amd64        Python 3 bindings for gobject-introspection libraries
ii  python3-gi-cairo                      3.38.0-2                        amd64        Python 3 Cairo bindings for the GObject library
ii  python3-httplib2                      0.18.1-3                        all          comprehensive HTTP client library written for Python3
ii  python3-ibus-1.0                      1.5.23-2                        all          Intelligent Input Bus - introspection overrides for Python (Python 3)
ii  python3-idna                          2.10-1                          all          Python IDNA2008 (RFC 5891) handling (Python 3)
ii  python3-ldb                           2:2.2.0-3.1                     amd64        Python 3 bindings for LDB
ii  python3-lib2to3                       3.9.2-1                         all          Interactive high-level object-oriented language (lib2to3)
ii  python3-louis                         3.16.0-1                        all          Python bindings for liblouis
ii  python3-mako                          1.1.3+ds1-2                     all          fast and lightweight templating for the Python 3 platform
ii  python3-markdown                      3.3.4-1                         all          text-to-HTML conversion library/tool (Python 3 version)
ii  python3-markupsafe                    1.1.1-1+b3                      amd64        HTML/XHTML/XML string library for Python 3
ii  python3-minimal                       3.9.2-3                         amd64        minimal subset of the Python language (default python3 version)
ii  python3-natsort                       7.1.0-1                         all          Natural sorting for Python (Python3)
ii  python3-olefile                       0.46-3                          all          Python module to read/write MS OLE2 files
ii  python3-pbr                           5.5.0-2                         all          inject useful and sensible default behaviors into setuptools - Python 3.x
ii  python3-pil:amd64                     8.1.2+dfsg-0.3                  amd64        Python Imaging Library (Python3)
ii  python3-pip                           20.3.4-4                        all          Python package installer
ii  python3-pkg-resources                 52.0.0-4                        all          Package Discovery and Resource Access using pkg_resources
ii  python3-pyatspi                       2.38.1-1                        all          Assistive Technology Service Provider Interface - Python3 bindings
ii  python3-pycurl                        7.43.0.6-5                      amd64        Python bindings to libcurl (Python 3)
ii  python3-pygments                      2.7.1+dfsg-2.1                  all          syntax highlighting package written in Python 3
ii  python3-pysimplesoap                  1.16.2-3                        all          simple and lightweight SOAP Library (Python 3)
ii  python3-reportbug                     7.10.3+deb11u1                  all          Python modules for interacting with bug tracking systems
ii  python3-requests                      2.25.1+dfsg-2                   all          elegant and simple HTTP library for Python3, built for human beings
ii  python3-setuptools                    52.0.0-4                        all          Python3 Distutils Enhancements
ii  python3-six                           1.16.0-2                        all          Python 2 and 3 compatibility library (Python 3 interface)
ii  python3-smbc                          1.0.23-1+b1                     amd64        Python 3 bindings for the Samba client library
ii  python3-software-properties           0.96.20.2-2.1                   all          manage the repositories that you install software from
ii  python3-speechd                       0.10.2-2+deb11u1                all          Python interface to Speech Dispatcher
ii  python3-talloc:amd64                  2.3.1-2+b1                      amd64        hierarchical pool based memory allocator - Python3 bindings
ii  python3-uno                           1:7.0.4-4+deb11u1               amd64        Python-UNO bridge
ii  python3-urllib3                       1.26.5-1~exp1                   all          HTTP library with thread-safe connection pooling for Python3
ii  python3-venv                          3.9.2-3                         amd64        venv module for python3 (default python3 version)
ii  python3-wheel                         0.34.2-1                        all          built-package format for Python
ii  python3-wxgtk4.0                      4.0.7+dfsg-10                   amd64        Python 3 interface to the wxWidgets Cross-platform C++ GUI toolkit
ii  python3-xdg                           0.27-2                          all          Python 3 library to access freedesktop.org standards
ii  python3-yaml                          5.3.1-5                         amd64        YAML parser and emitter for Python3
ii  python3.9                             3.9.2-1                         amd64        Interactive high-level object-oriented language (version 3.9)
ii  python3.9-dbg                         3.9.2-1                         amd64        Debug Build of the Python Interpreter (version 3.9)
ii  python3.9-dev                         3.9.2-1                         amd64        Header files and a static library for Python (v3.9)
ii  python3.9-minimal                     3.9.2-1                         amd64        Minimal subset of the Python language (version 3.9)
ii  python3.9-venv                        3.9.2-1                         amd64        Interactive high-level object-oriented language (pyvenv binary, version 3.9)
```





