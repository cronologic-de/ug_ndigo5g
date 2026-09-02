=============
API Reference
=============

The API is a DLL with C linkage.

The interface is provided via ``Ndigo_interface.h``, which is provided
with the Ndigo5G driver. The driver can be downloaded from our
`Ndigo5G product page <https://www.cronologic.de/product/ndigo5g-10>`__.

By default, the installer will copy the interface and library files to
``C:\Program Files\cronologic\NdigoSeries\driver``.

When compiling, all interface ``.h`` and library ``.lib`` files must be
discoverable by your compiler and linker. They are located in ``include\`` and
``x64\`` (or ``x64_32``, if you are on a 32-bit system), respectively.

When running your program the dynamic link library DLLs containing the 
actual driver code must reside in the same directory as your executable or be
in a directory included in the PATH variable.
Note that for Linux, the library files are provided only as a static ``.a``
library.

**Setting up and using an Ndigo5G**

Setting up and using a Ndigo5G in your application software requires that you:

- Initialize an Ndigo5G device (see :doc:`initialization`).
- Configure the initialized Ndigo5G device (see :doc:`configuration`).
- Start data acquisition (see :doc:`runtime_control`).
- Read data from the device (see :doc:`readout`).
- Process the data provided as packets (see :doc:`data_format`).


.. raw:: html

    <h2>Contents</h2>

.. toctree::
    :maxdepth: 2

    initialization
    configuration
    runtime_control
    readout
    data_format
    status_information
    driver_information
    led_controls
    constants
