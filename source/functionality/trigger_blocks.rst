==============
Trigger Blocks
==============


Ndigo5G-10 record analog waveforms using
:doc:`zero suppression <zero_suppression>`.


Whenever a relevant waveform is detected, data is written to an internal
FIFO memory.
Each ADC channel has one trigger block determining whether
data is written to the FIFO. The trigger blocks are configured
using :member:`ndigo_configuration::trigger_block`.


Each trigger block consists of two independent units that check the
incoming raw data stream for trigger conditions
(:numref:`fig zero supp`). The triggers of each trigger block can be configured
to use level triggering (trigger if the signal level is above or below a
threshold) or edge triggering (trigger if the signal level crosses-over a
set threshold).


Level or edge triggering is configured using :member:`ndigo_trigger::edge`.


The recording window can be configured using
:member:`ndigo_trigger_block::precursor` and
:member:`ndigo_trigger_block::length`, as highlighted in
:numref:`fig edge trigger` and :numref:`fig level trigger`.


.. figure:: ../_figures/edge-trigger.*
    :name: fig edge trigger
    :alt: Principle of edge triggering for cronologic's Ndigo5G.

    Parameters for edge triggering.


.. figure:: ../_figures/level-trigger.*
    :name: fig level trigger
    :alt: Principle of edge triggering for cronologic's Ndigo5G.

    Parameters for level triggering.


When using edge triggering, all packets have the same length of
*precursor* + *length* + 1 cycles of 3.2 ns.


For level triggering, packet length is data dependent.


Note that triggering is not accurate to sample.
For each 3.2 ns clock cycle, it is determined whether for any sample during
that clock cycle a trigger condition is met.
That clock cycle is then selected as the trigger point.
As a result, the trigger sample can be anywhere
within a range of up to 16 samples depending on the
:doc:`ADC mode <adc_modes>`, as highlighted in the following figures.


.. figure:: ../_figures/1ChannelTriggering.*
    :name: fig one channel triggering
    :alt: Example trigger configuration for 1-channel mode for cronologic'
          Ndigo5G digitizer.
        
    Triggering in 1-channel mode at 16 samples per clock cycle.


.. figure:: ../_figures/2ChannelTriggering.*
    :name: fig two channel triggering
    :alt: Example trigger configuration for 2-channel mode for cronologic'
          Ndigo5G digitizer.
        
    Triggering in 2-channel mode at 8 samples per clock cycle.


.. figure:: ../_figures/4ChannelTriggering.*
    :name: fig four channel triggering
    :alt: Example trigger configuration for 4-channel mode for cronologic'
          Ndigo5G digitizer.
        
    Triggering in 4-channel mode at 4 samples per clock cycle.


If re-triggering is active, the current trigger window is extended if a
trigger event is detected inside the window.


A trigger block can use several input sources:

- the 8 trigger decision units of all four ADC channels
  (:numref:`fig analog trigger`)
- the GATE input (:numref:`fig digital trigger`)
- the Trigger or TDC input (:numref:`fig digital trigger`)
- a function trigger providing random or periodic triggering
  (:doc:`auto_trigger`)
- triggers originating from other cards connected with the sync cable
  or from the Ndigo Extension card (BUS0, BUS1, BUS2, BUS3)
  (:numref:`fig extension block`)
- A second set of trigger units with names ending in ``PE`` for the digital
  inputs Trigger, GATE, BUS0, BUS1, BUS2, and BUS3, configured for
  positive edge triggering.
  Together with the regular trigger units on
  these inputs, both edges of a pulse can be used in the trigger logic.
  However, this set of triggers is not available as inputs for the
  :doc:`gating blocks <gating_blocks>`.


Trigger inputs from the above sources can be concatenated using a logical
“OR” (see :numref:`fig trigger matrix`) by
setting the appropriate bits in :member:`trigger_blocks::sources` bitmask.


.. figure:: ../_figures/analog-trigger.*
    :alt: Schematic of the trigger unit for the analog channels of cronologic's
          Ndigo5G digitizer.
    :name: fig analog trigger
    :width: 60%

    From the ADC inputs, a trigger unit creates an input flag for the
    :ref:`trigger matrix <fig trigger matrix>`.
    Each analog digitizer channel (A, B, C, D) has two trigger units.


.. figure:: ../_figures/DigitalInput.*
    :alt: Schematic of the trigger unit for the digital channels of cronologic's
          Ndigo5G digitizer.
    :name: fig digital trigger
    :width: 40%

    From the digital inputs Trigger, Gate, BUS0, BUS1, BUS2, and BUS3, a
    trigger unit creates an input flag for the
    :ref:`trigger matrix <fig trigger matrix>`.


.. figure:: ../_figures/ExtensionBlock.*
    :alt: Combined signals from the extension block of cronologic's
          Ndigo5G digitizer.
    :name: fig extension block
    :width: 40%

    The extension block combines signals from the optional extension board
    and the sync cable.

.. figure:: ../_figures/triggermatrix.*
    :alt: Trigger matrix of each ADC channel of cronologic's Ndigo5G digitizer.
    :name: fig trigger matrix

    The trigger matrix combines triggers from all trigger units as
    inputs for the trigger blocks. The four gate units can be
    used to suppress the combined trigger.


Triggers can also be fed into the :doc:`gating blocks <gating_blocks>`.
Gate blocks can be used to block writing data to the FIFO.
That way, only zero suppressed data occurring when the selected gate is active
is transmitted.
This procedure reduces the PCIe bus load even further.
