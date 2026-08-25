.. raw:: latex

    \clearpage

:tocdepth: 3

============
Data Readout
============

The device provides a stream of *packets* (see :doc:`data_format`)
that are read in batches with :func:`ndigo_read`.

:func:`ndigo_read` requires :struct:`ndigo_read_in` as configuration.

:func:`ndigo_read` stores the read batch in a :struct:`ndigo_read_out`
struct.

Every packet needs to be *acknowledged* before its memory location can be used
again by the Ndigo5G device.

A typical workflow in an application would be:

- Start data acquisition (see :doc:`runtime_control`).
- Read a batch of packets.
- Iterate through the batch and process the packets (see :doc:`data_format`
  for the data layout). For this purpose, :c:macro:`ndigo_next_packet` is
  provided.
- Acknowledge the batch as processed with :func:`ndigo_acknowledge`.

Instead of manually acknowledging each batch, each read batch of data can be
automatically acknowledged by setting
:member:`ndigo_read_in::acknowledge_last_read` to true.

The following example highlights the workflow.
A complete coding example can be found on
`github.com/cronologic-de/ndigo5g_babel <https://github.com/cronologic-de/ndigo5g_babel>`__
or in :doc:`../code_example/index`.

.. code-block:: C

    ndigo_read_in read_config;
    read_config.acknowledge_last_read = true;
    ndigo_read_out read_data;

    status = ndigo_read(device, &read_config, &read_data)
    if (status != ndigo_OK) {
        // handle errors of the call to timetagger4_read
    }
    else if (read_data.error_code != ndigo_READ_OK)
    {
        // handle read errors, e.g., empty packets
    }
    else
    {
        volatile ndigo_packet *p = read_data.first_packet;
        while (p <= read_data.last_packet)
        {

            /* process data */

            p = ndigo_next_packet(p);
        }
    }


.. latex-toc-doxygenfunction:: ndigo_read

.. latex-toc-doxygenfunction:: ndigo_acknowledge

.. latex-toc-doxygenstruct:: ndigo_read_in

.. latex-toc-doxygenstruct:: ndigo_read_out

.. latex-toc-doxygenfunction:: ndigo_process_tdc_packet

.. latex-toc-doxygenfunction:: ndigo_convert_value

.. latex-toc-doxygendefine:: ndigo_next_packet
    :hide-initializer:
