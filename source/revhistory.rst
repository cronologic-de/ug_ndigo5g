================
Revision History
================


Firmware
========


1.5417 — 2024-05-08
    | Bug fixes

1.5412 — 2022-05-02
    | Support for Ndigo5G-S board variant

1.4937 — 2019-04-01
    | TiGer added

1.4865 — 2015-07-28
    | Internal optimizations

1.4824 — 2015-02-27
    | Fixed intel PCIe link training issues



Driver and Applications
=======================

1.6.2 — TBD
    | TBD

1.6.1 — 2026-09-14
    | Enhanced IOMMU compatibility: The kernel-mode driver now enables full DMA
      support, ensuring seamless operation when IOMMU is active
    | Updated docstrings in interface files

1.5.12 — 2024-06-27
    | Revert HPTDC8-PCI support to v3.9.5 on ``crono_tools``

1.5.8 — 2023-10-25
    | Added new :struct:`crono_pcie_info` structure with PCIe error flags

1.5.4 — 2023-09-09
    | Fixed TDC calibration

1.5.3 — 2023-08-30
    | Hardware Revision 5+ Support
    | Added new fields to static info

1.4.4 — 2022-05-12
    | Fixed broken backup in firmware tool and display errors in NdigoScope

1.4.3 — 2019-10-21
    | Fixed a card initialization error in x64 32 mode

1.4.0 — 2019-06-04
    | Added Windows 10 support

1.3.0 — 2017-06-08
    | NdigoScope application now supports Ndigo250M-14



User Guide
==========
2.1.0 — TBD
    | Fixed incorrect documentation for :member:`ndigo_configuration::dc_offset`
    | Added documentation for :c:macro:`NDIGO_READ_WRONG_STATE`
    | Updated driver revision list
    | Minor fixes

2.0.0 — 2026-09-14
    | Added HTML version of user guide
    | Updated driver revision list

1.3.7 — 2026-08-26
    | Documented thermal baseline drift after initialization

1.3.5 — 2026-04-15
    | Updated Driver Revision list

1.3.4 — 2025-11-04
    | Documented multishot mode in API
    | Added Table 2.1

1.3.3 — 2025-10-17
    | Minor improvements and corrections

1.3.2 — 2024-12-10
    | Updated firmware revision list

1.3.1 — 2024-10-31
    | Expanded installation instructions
    | Updated Erratum

1.3.0 — 2024-10-01
    | Added section “Memory Management”
    | Renamed DMA buffer to host buffer
    | Updated Figure 2.21
    | Added defaults to API
    | Updated Export Control
    | Added guaranteed cutoff frequencies

1.2.5 — 2024-06-27
    | Added Ndigo Crate as a possible solution to the PCIe 5.0 bug
    | Updated Driver Revisions

1.2.4 — 2024-06-12
    | Fixed documentation for :doc:`functionality/auto_trigger`
    | Updated Export Control
    | Updated Technical Data
    | Updated Feature List
    | Updated C Example
    | Documented known bug related to PCIe 5.0

1.2.3 — 2024-03-22
    | Adjusted styling

1.2.2 — 2022-11-04
    | Documented bug: Ndigo5G does not work in Thunderbolt enclosures
    | Reduced temperature range
    | Improved ADC characteristics due to tighter production tests
    | Added dual use disclaimer
    | Clarified _pe positive edge triggers
    | Corrected polarity for dc_offset
    | Corrected extension card clock from 39 MHz to 39.0625 MHz
    | Analog Bandwidth clarifications and corrections

1.2.1 — 2020-09-20
    | Cosmetic changes

1.1.3 — 2020-11-27
    | Dual-Use information

1.1.2 — 2019-10-27

1.1.0 — 2019-08-27
    | API clarifications
