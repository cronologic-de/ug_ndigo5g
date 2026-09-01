=========
ADC Modes
=========

The Ndigo5G-10 quantizes the input signal to 8 bits. However, the board always
scales and offsets the data to 16-bit signed data centered around 0.


Data processing such as trigger detection or packet building are always
performed on 3.2 ns intervals.
Depending on the ADC mode, this interval may contain 4, 8 or 16 samples.


The board supports using one, two or four channels.



1-Channel Modes A, B, C, and D
==============================


In these modes, only a single channel is used.
The analog signal on that channel is digitized at 5 Gsps.


Packet size is always a multiple of 16 samples per 3.2 ns.


:numref:`fig one channel mode` shows the signal routing for this mode.


:numref:`fig one channel triggering` in :doc:`trigger_blocks`
shows triggering in 1-channel mode.


.. figure:: ../_figures/1ChannelMode.*
    :name: fig one channel mode
    :alt: ADCs of cronologic's Ndigo5G digitizer in 1-channel mode.

    ADCs in 1-channel mode, interleaved for 5 Gsps.



2-Channel Modes AC, BC, AD, and BD
==================================


In these modes, two channels are used simultaneously.
The analog signals on these channels are digitized at 2.5 Gsps each.


Packet size is always a multiple of 8 samples per 3.2 ns.


:numref:`fig two channel mode` shows the signal routing for this mode.


:numref:`fig two channel triggering` in :doc:`trigger_blocks`
shows triggering in 1-channel mode.


.. figure:: ../_figures/2ChannelMode.*
    :name: fig two channel mode
    :alt: ADCs of cronologic's Ndigo5G digitizer in 2-channel mode.

    ADCs in 2-channel mode, interleaved for 2.5 Gsps.



4-Channel Mode ABCD
===================


In this mode, all four channels are digitized independently at 1.25 Gsps each.


The packet size is always a multiple of 4 samples per 3.2 ns.


:numref:`fig four channel mode` shows the signal routing for this mode.


:numref:`fig four channel triggering` in :doc:`trigger_blocks`
shows triggering in 1-channel mode.


.. figure:: ../_figures/4ChannelMode.*
    :name: fig four channel mode
    :alt: ADCs of cronologic's Ndigo5G digitizer in 4-channel mode.

    ADCs in 4-channel mode, interleaved for 1.25 Gsps.



Multiple-Sampling Modes AAAA, BBBB, CCCC and DDDD
=================================================


In these modes, only one analog input channel is used, but the channel
is sampled independently and simultaneously by the four ADCs at 1.25 Gsps.


The board creates four independent streams with 4 samples each per 3.2 ns.


Using the same trigger setting on all ADCs, the multi-sampling modes can be
used to reduce noise by averaging the four channels.


To deal with complex triggering conditions, different trigger settings on each
of the ADCs can be used.


The Ndigo5G provides 4 ADCs sampling at 1.25 Gsps each. Higher speed
modes are implemented by interleaving two or four of these ADCs.


During interleaving, the Ndigo5G firmware reorders and groups the data
into a linear sample stream. The process is fully transparent.

For users, the only difference is that a 3.2 ns cycle can contain 4, 8 or 16
samples, depending on the mode.
