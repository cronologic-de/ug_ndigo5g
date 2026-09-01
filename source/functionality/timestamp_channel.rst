=================
Timestamp Channel
=================


The timestamp channel produces a stream of small packets that denote the
time of the trigger event.

An arbitrary set of trigger sources can be
selected in the trigger matrix to cause the creation of
an :struct:`ndigo_packet`.


The packets have a fixed length of 16 bytes.


The :member:`~ndigo_packet::length` field of the packet contains a 32 bit
pattern that contains the levels of all trigger sources at the time of the
trigger event except for the period monitor.


Only one packet is created, no matter how many trigger sources caused the
timestamp channel to trigger.
