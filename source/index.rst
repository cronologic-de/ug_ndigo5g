=====================
Ndigo5G-10 User Guide
=====================

.. raw:: latex

    \RaggedRight

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{chapter}{Introduction}
    \chapter*{Introduction}
    \markboth{Introduction}{}

The Ndigo5G is a digitizer and transient recorder designed to sample
relatively shorts pulses in rapid repetition. It produces a stream of
output packets, each containing data from a single trigger event
together with a timestamp.

.. only:: latex

    This User Guide is also available online at
    `docs.cronologic.de/ndigo5g <https://docs.cronologic.de/ndigo5g>`_.


**Features**

-  10 bit dynamic range
-  Up to 5 Gsps sample rate (in 1-channel mode)
-  Up to four ADC channels with configurable DC offsets
-  Two digital control inputs for gating and triggering, one of which
   can be used as a TDC
-  Advanced zero suppression to massively reduce data load
-  PCIe 1.1 x4 interface with 800 MB/s throughput
-  Possibility to synchronize up to eight boards
-  Extension board with four additional digital inputs
-  Onboard 10 MHz oscillator with a stability of 10 ppb, or possibility
   to use external 10 MHz clock

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    hardware
    functionality/index
    api_reference/index
    code_example/index
    technical_data
    revhistory
