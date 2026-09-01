================
Zero Suppression
================


One of Ndigo5G’s key features is on-board zero suppression to reduce
PCIe bus load.

Only data that passes specifications predefined by the
user is transmitted.

This guide refers to transmitted waveform data as
:struct:`packets <ndigo_packet>`.

A packet contains the waveform data and a timestamp giving
the absolute time (i.e., the time since start of data acquisition) of
the packet’s last sample.


:numref:`fig zero supp` shows a simple example:
Data is written to the PC only if values exceed a specified threshold.


Expanding on that, Ndigo5G’s zero suppression can be used to realize
much more complex scenarios.


.. figure:: ../_figures/ZeroSupp.*
    :name: fig zero supp
    :alt: Simple zero suppression for cronologic's Ndigo5G.

    Simple zero suppression: Only data with values above a threshold
    are streamed to the PC.
