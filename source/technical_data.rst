==============
Technical Data
==============


**Input Passband**: 4.5 MHz to 950 MHz.

**Power Requirements**: 25 W

**Mechanical Dimensions** (excluding slot bracket): 170 mm × 111.15 mm

**Throughput**: 800 MByte/s on PCIe x4



Digitizer Characteristics
=========================


Each board is tested against the values listed in the “Min” column.
“Typical” is the mean value of the first 10 boards produced.



1-Channel-Mode (5Gsps)
----------------------


+---------------------+--------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                | Min | Typical | Max | Units |
+=====================+==========================+=====+=========+=====+=======+
| THD\ :sub:`1`       | Total Harmonic           |     | –60     | –56 | dB    |
|                     | Distortion               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`1`       | Signal to Noise Ration   | 47  | 49      |     | dB    |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,1` | Spurious Free Dynamic    | 55  | 59      |     | dB    |
|                     | Range (including         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,1` | Spurious Free Dynamic    | 55  | 60      |     | dB    |
|                     | Range (excluding         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`1`     | Signal-to-Interference   | 47  | 48      |     | dB    |
|                     | Ratio including Noise    |     |         |     |       |
|                     | and Distortion           |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`1`      | Effective Number of Bits | 7.5 | 7.7     |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+



2-Channel-Mode (2.5 Gsps)
-------------------------


+---------------------+--------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                | Min | Typical | Max | Units |
+=====================+==========================+=====+=========+=====+=======+
| THD\ :sub:`2`       | Total Harmonic           |     | –60     | –56 | dB    |
|                     | Distortion               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`2`       | Signal to Noise Ration   | 49  | 51      |     | dB    |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,2` | Spurious Free Dynamic    | 58  | 60      |     | dB    |
|                     | Range (including         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,2` | Spurious Free Dynamic    | 58  | 61      |     | dB    |
|                     | Range (excluding         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`2`     | Signal-to-Interference   | 49  | 50      |     | dB    |
|                     | Ratio including Noise    |     |         |     |       |
|                     | and Distortion           |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`2`      | Effective Number of Bits | 7.8 | 8.1     |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+




4-Channel-Mode (1.25 Gsps)
--------------------------


+---------------------+--------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                | Min | Typical | Max | Units |
+=====================+==========================+=====+=========+=====+=======+
| THD\ :sub:`4`       | Total Harmonic           |     | –60     | –56 | dB    |
|                     | Distortion               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`4`       | Signal to Noise Ration   | 49  | 51      |     | dB    |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,4` | Spurious Free Dynamic    | 58  | 60      |     | dB    |
|                     | Range (including         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,4` | Spurious Free Dynamic    | 68  | 73      |     | dB    |
|                     | Range (excluding         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`4`     | Signal-to-Interference   | 49  | 51      |     | dB    |
|                     | Ratio including Noise    |     |         |     |       |
|                     | and Distortion           |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`4`      | Effective Number of Bits | 7.9 | 8.1     |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+




Oscillator
==========


+-----------------+-------------------------+-----+---------+------+-------+
| Symbol          | Parameter               | Min | Typical | Max  | Units |
+=================+=========================+=====+=========+======+=======+
| ΔT              | Stability in            |     |         | 10   | ppb   |
|                 | temperature range       |     |         |      |       |
|                 | −20 °C–70 °C\ :sup:`1`  |     |         |      |       |
+-----------------+-------------------------+-----+---------+------+-------+
| F               | Initial calibration     |     | <300    | 500  | ppb   |
+-----------------+-------------------------+-----+---------+------+-------+
| ΔF/F\ :sub:`1`  | Aging first year        |     |         | 100  | ppb   |
+-----------------+-------------------------+-----+---------+------+-------+
| ΔF/F\ :sub:`20` | All inclusive aging 20  |     |         | 1000 | ppb   |
|                 | years                   |     |         |      |       |
+-----------------+-------------------------+-----+---------+------+-------+
|                 | Warm-up\ :sup:`2`       |     |         | 3    | min.  |
+-----------------+-------------------------+-----+---------+------+-------+

:sup:`1`\ Over –40 °C to +85 °C; relative to stabilized frequency
after 1 hour of continuous operation

:sup:`2` @+25 °C; within ±100 ppb of F, where F is the stabilized frequency
reached after 1 hour of continuous operation



Electrical Characteristics
==========================



.. _sec environmental:

Environmental Conditions for Operation
--------------------------------------


The board is designed to be operated under the following conditions:


+--------+----------------+-----+---------+-----+----------------+
| Symbol | Parameter      | Min | Typical | Max | Units          |
+========+================+=====+=========+=====+================+
| T      | ambient        | 5   |         | 40  | Celsius        |
|        | temperature    |     |         |     |                |
+--------+----------------+-----+---------+-----+----------------+
| RH     | relative       | 20  |         | 75  | %              |
|        | humidity at    |     |         |     |                |
|        | 31 °C          |     |         |     |                |
+--------+----------------+-----+---------+-----+----------------+



.. _sec storage:

Environmental Conditions for Storage
------------------------------------


The board shall be stored between operation under the following
conditions:


+--------+----------------+-----+---------+-----+----------------+
| Symbol | Parameter      | Min | Typical | Max | Units          |
+========+================+=====+=========+=====+================+
| T      | ambient        | –30 |         | 60  | Celsius        |
|        | temperature    |     |         |     |                |
+--------+----------------+-----+---------+-----+----------------+
| RH     | relative       | 10  |         | 70  | %              |
|        | humidity at    |     |         |     |                |
|        | 31 °C          |     |         |     |                |
|        | non-condensing |     |         |     |                |
+--------+----------------+-----+---------+-----+----------------+



Power Supply
------------


=============== ================================= ==== ======= ==== =====
Symbol          Parameter                         Min  Typical Max  Units
=============== ================================= ==== ======= ==== =====
I\ :sub:`3.3`   PCIe 3.3 V rail power consumption              4    mA
VCC\ :sub:`3.3` PCIe 3.3 V rail power supply      3.1  3.3     3.6  V
I\ :sub:`12`    PCIe 12 V rail power consumption               2.1  A
VCC\ :sub:`12`  PCIe 12 V rail power supply       11.1 12      12.9 V
I\ :sub:`aux`   PCIe 3.3 V rail power consumption      0            A
VCC\ :sub:`aux` PCIe 3.3 V rail power supply           3.3          V
=============== ================================= ==== ======= ==== =====



Analog Inputs
-------------


AC coupled single-ended analog inputs (standard version).


================ ========================== ===== ======= ==== ==============
Symbol           Parameter                  Min   Typical Max  Units
================ ========================== ===== ======= ==== ==============
V\ :sub:`p-p`    Peak to peak input voltage               0.5  V
Z\ :sub:`P`      Input impedance                  50           Ω
V\ :sub:`adcofs` Analog offset              –0.25         0.25 V
================ ========================== ===== ======= ==== ==============


AC coupled differential analog inputs (S version).


================ ========================== ===== ======= ==== ==============
Symbol           Parameter                  Min   Typical Max  Units
================ ========================== ===== ======= ==== ==============
V\ :sub:`com`    Input common mode          –4            6    V
V\ :sub:`p-p`    Differential input Voltage –125          125  mV
Z\ :sub:`P`      Input impedance                  100          Ω
V\ :sub:`adcofs` Analog offset              –0.25         0.25 V
================ ========================== ===== ======= ==== ==============


Guaranteed cutoff frequencies (standard version)


+---------------------+----------------------------------------------+------+---------+-----+-------+
| Symbol              | Parameter                                    | Min  | Typical | Max | Units |
+=====================+==============================================+======+=========+=====+=======+
| f\ :sub:`c,limited` | Upper cutoff frequency for limited bandwidth |      |         |     |       |
+---------------------+----------------------------------------------+------+---------+-----+-------+
|                     | 3 dB                                         | 800  |         |     | MHz   |
+---------------------+----------------------------------------------+------+---------+-----+-------+
|                     | 6 dB                                         | 1400 |         |     | MHz   |
+---------------------+----------------------------------------------+------+---------+-----+-------+
| f\ :sub:`c,full`    | Upper cutoff frequency for full bandwidth    |      |         |     |       |
+---------------------+----------------------------------------------+------+---------+-----+-------+
|                     | 3 dB                                         | 1000 |         |     | MHz   |
+---------------------+----------------------------------------------+------+---------+-----+-------+
|                     | 6 dB                                         | 1900 |         |     | MHz   |
+---------------------+----------------------------------------------+------+---------+-----+-------+



Guaranteed cutoff frequencies (S version, Revs. C and D)


+---------------------+----------------------------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                                    | Min | Typical | Max | Units |
+=====================+==============================================+=====+=========+=====+=======+
| f\ :sub:`c,limited` | Upper cutoff frequency for limited bandwidth |     |         |     |       |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 3 dB                                         | 70  |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 6 dB                                         | 115 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
| f\ :sub:`c,full`    | Upper cutoff frequency for full bandwidth    |     |         |     |       |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 3 dB                                         | 70  |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 6 dB                                         | 115 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+


Guaranteed cutoff frequencies (S version, Rev. E)


+---------------------+----------------------------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                                    | Min | Typical | Max | Units |
+=====================+==============================================+=====+=========+=====+=======+
| f\ :sub:`c,limited` | Upper cutoff frequency for limited bandwidth |     |         |     |       |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 3 dB                                         | 180 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 6 dB                                         | 300 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
| f\ :sub:`c,full`    | Upper cutoff frequency for full bandwidth    |     |         |     |       |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 3 dB                                         | 180 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+
|                     | 6 dB                                         | 330 |         |     | MHz   |
+---------------------+----------------------------------------------+-----+---------+-----+-------+



Digital Inputs
--------------


Single ended AC coupled inputs Trigger and GATE with configurable DC
offset bias.


================= ================= ===== ======= ===== ==============
Symbol            Parameter         Min   Typical Max   Units
================= ================= ===== ======= ===== ==============
V\ :sub:`trig`    Pulse height                    5.0   V
V\ :sub:`trigofs` DC offset         –1.25         1.25  V
V\ :sub:`TDCofs`  DC offset for TDC –1.25         –0.01 V
Z\ :sub:`trig`    Input impedance         50            Ω
t\ :sub:`pulse`   Pulse width       7             100   ns
================= ================= ===== ======= ===== ==============



Information Required by DIN EN 61010-1
======================================


.. _sec address:

Manufacturer
------------


The Ndigo5G is a product of:

   | cronologic GmbH & Co. KG
   | Jahnstraße 49
   | 60318 Frankfurt
   |
   | HRA 42869 beim Amtsgericht Frankfurt/M
   | VAT-ID: DE235184378



Intended Use and System Integration
-----------------------------------


The devices are not ready to use as delivered by cronologic. It requires
the development of specialized software to fulfill the application of
the end user. The device is provided to system integrators to be built
into measurement systems that are distributed to end users. These
systems usually consist of a Ndigo5G, a main board, a case, application
software and possible additional electronics to attach the system to
some type of detector. They might also be integrated with the detector.

The Ndigo5G is designed to comply with DIN EN 61326-1 when operated on a
PCIe compliant main board housed in a properly shielded enclosure. When
operated in a closed standard compliant PC enclosure the device does not
pose any hazards as defined by EN 61010-1.

Radiated emissions, noise immunity and safety highly depend on the
quality of the enclosure. It is the responsibility of the system
integrator to ensure that the assembled system is compliant to
applicable standards of the country that the system is operated in,
especially regarding user safety and electromagnetic interference.
Compliance was only tested for attached cables shorter than 3 m.

When handling the board, adequate measures have to be taken to protect
the circuits against electrostatic discharge (ESD). All power supplied
to the system must be turned off before installing the board.



Cooling
-------


The Ndigo5G in its base configuration has passive cooling that requires
a certain amount of air flow. If the case design cannot provide enough
air flow to the board, a slot cooler like the Zalman ZM-SC100 can be placed
next to the board. Active cooling is also available as an option to the
board.



Environmental Conditions
------------------------


See :ref:`sec environmental` and :ref:`sec storage`.



Inputs
------


All inputs are AC coupled. The inputs have very high input bandwidth
requirements and therefore there are no circuits that provide
over-voltage protection for these signals. Any voltage on the inputs
above 5 V or below –5 V relative to the voltage of the slot
cover can result in permanent damage to the board.



.. _sec erratum:

Erratum
-------



Thunderbolt
~~~~~~~~~~~


The Ndigo5G does not work in most Thunderbolt PCIe extension enclosures.
The reason is unknown.


Workarounds:

-  Use the Ndigo6G. All other cronologic products work reliably in
   Thunderbolt enclosures. The Ndigo6G offers very similar functionality
   to the Ndigo5G at a higher performance.\ :sup:`1`



PCIe 5.0
~~~~~~~~


The Ndigo5G might not work in PCIe 5.0 slots that support the “Enhanced
Link Behavior Control” feature.


Workarounds:

-  Disable “Enhanced Link Behavior Control” in BIOS.
-  Limit PCIe transfer rates to transfer rates of up to PCIe 4.
-  If your main board has PCIe slots that are not PCIe 5.0, install your
   Ndigo5G in these.
-  Use Ndigo6G. The Ndigo6G works reliably in PCIe 5.0 slots while
   offering similar functionality.\ :sup:`1`


:sup:`1` When using the Ndigo6G as a replacement, there are some
software changes required in the device configuration. The readout
data format and API is largely identical. See
`www.cronologic.de/products/adcs/ndigo6g-12 <https://www.cronologic.de/products/adcs/ndigo6g-12>`__
for details.



PCIe Connector
~~~~~~~~~~~~~~


Some electrical components on the Ndigo5G-10 and Ndigo5G-S-C boards are
placed close to the PCIe connector, and thus may, in rare cases, get
shorted by metal shielding elements of the PCIe slot of the mainboard.
This will neither damage the Ndigo5G board nor the mainboard, however,
the shortened PCIe lanes will not be functional.


Make sure to follow the installation instructions in
:ref:`sec installation`.



Recycling
---------


cronologic is registered with the “Stiftung Elektro-Altgeräte Register”
as a manufacturer of electronic systems with Registration ID
DE 77895909.

The Ndigo5G belongs to category 9, “Überwachungs und Kontrollinstrumente
für ausschließlich gewerbliche Nutzung.” The last owner of an Ndigo5G
must recycle it, treat the board in compliance with §11 and §12 of the
German ElektroG, or return it to the manufacturer’s address listed
:ref:`above <sec address>`.



Export Control
--------------


The Ndigo5G product line is a dual use item under
`Council Regulation (EC) No 428/2009 of 5 May 2009 <https://eur-lex.europa.eu/eli/reg/2009/428/oj>`__
in section 3A002h. Similar regulations exist in many countries outside Europe.


Regardless of the fact that we at cronologic exclude the use of our
products for military purposes, **the laws of the EU and many other
countries restrict exports** of dual-use items. Since we have to apply
for a **General Export Permit** for these countries, delivery processes
may be delayed or delivery to certain countries may become impossible.


For the application of this
`export license <https://www.cronologic.de/faq/export-license>`__, we need the
following documents from you:


-  Exporter declaration
-  Company profile
-  Import license (country dependent)


There are countries for which a **General Export License** can be used
for the export of dual-use goods. In this case we need the corresponding
documents from you and there will be no further delay. These include:


-  Australia
-  Japan
-  Canada
-  Liechtenstein
-  New Zealand
-  Norway
-  Switzerland
-  Singapore
-  USA


Before re-exporting an Ndigo5G or any product containing an Ndigo5G as a
component, please check you local regulations whether an export permit
is required.


It is not permitted to export an Ndigo5G to the Russian Federation or
the Republic of Belarus.
