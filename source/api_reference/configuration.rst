.. raw:: latex

    \clearpage

:tocdepth: 3

=============
Configuration
=============

After an Ndigo5G device has been initialized (see :doc:`initialization`),
it must be configured before it can acquire data.

To configure an Ndigo5G device:

- Get a default set of configuration parameters using
  :func:`ndigo_get_default_configuration`.
- Change parameters of :struct:`ndigo_configuration` according to your
  specific requirements.
- Configure the Ndigo5G device using :func:`ndigo_configure`.

The following example shows a basic configuration of an already initialized
Ndigo5G device using the default configuration parameters.
A complete coding example can be found on
`github.com/cronologic-de/ndigo5g_babel <https://github.com/cronologic-de/ndigo5g_babel>`__
or in :doc:`../code_example/index`.

.. code-block:: C

    int status;

    // get a default set of configuration parameters
    ndigo_configuration config;
    status = ndigo_get_default_configuration(device, &config);
    if (status != NDIGO_OK) { /* handle error */ }

    // optionally modify config

    // configure the device
    status = ndigo_configure(device, &config);
    if (status != NDIGO_OK) { /* handle error */ }


.. latex-toc-doxygenfunction:: ndigo_get_default_configuration

.. latex-toc-doxygenfunction:: ndigo_configure

.. latex-toc-doxygenfunction:: ndigo_get_current_configuration

.. latex-toc-doxygenfunction:: ndigo_set_board_id

.. doxygentypedef:: lut_func


.. latex-toc-doxygenstruct:: ndigo_configuration

.. latex-toc-doxygenstruct:: ndigo_trigger

.. latex-toc-doxygenstruct:: ndigo_trigger_block

.. latex-toc-doxygenstruct:: ndigo_gating_block

.. latex-toc-doxygenstruct:: ndigo_extension_block
