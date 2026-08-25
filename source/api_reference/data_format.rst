.. raw:: latex

    \clearpage

:tocdepth: 3

==================
Output Data Format
==================

*Packets* are provided with :func:`ndigo_read` (see :doc:`readout`).

The following code snippet showcases how to unpack a packet containing
regular ADC data.
A complete coding example can be found on
`github.com/cronologic-de/ndigo5g_babel <https://github.com/cronologic-de/ndigo5g_babel>`__
or in :doc:`../code_example/index`.

.. code-block:: c

    bool = is_timestamp_only = packet->type & NDIGO_PACKET_TYPE_TIMESTAMP_ONLY;

    printf("Card %d, Channel %d, Flags %d, Length %d, Timestamp %lu \n",
           packet->card,
           packet->channel,
           packet->flags,
           is_timestamp_only ? 0 : packet->length,
           packet->timestamp);

    if (!is_timestamp_only)
    {
        short* data = (short*)packet->data;
        for (unsigned int i = 0; i < packet->length * 4; i++)
            printf("%6d, ", *(data++));
        printf("\n\n");
    }

.. latex-toc-doxygenstruct:: ndigo_packet