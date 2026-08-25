.. raw:: latex

    \clearpage

:tocdepth: 3

.. _sec initialization:

==============
Initialization
==============

To initialize an Ndigo5G:

- Get a default set of initialization parameters using
  :func:`ndigo_get_default_init_parameters`.
- Change parameters of :struct:`ndigo_init_parameters` according to your
  specific requirements.
- Initialize an Ndigo5G device using :func:`ndigo_init`.
- Release all resources using :func:`ndigo_close`.

The following example shows a basic setup of an Ndigo5G using the default
initialization parameters.
A complete coding example can be found on
`github.com/cronologic-de/ndigo5g_babel <https://github.com/cronologic-de/ndigo5g_babel>`__
or in :doc:`../code_example/index`.

.. code-block:: C

    int status;

    // get a default set of initialization parameters
    ndigo_init_parameters params;
    status = ndigo_get_default_init_parameters(&params);
    if (status != NDIGO_OK) { /* handle error */ }

    // initialize a device
    const char* err_message;
    ndigo_device* device = ndigo_init(&params, &status, &err_message);
    if (status != NDIGO_OK) { /* handle error */ }

    // use device

    // after usage, free up all resources by closing the device
    status = ndigo_close(device)


.. latex-toc-doxygenfunction:: ndigo_get_default_init_parameters

.. latex-toc-doxygenfunction:: ndigo_init

.. latex-toc-doxygenfunction:: ndigo_close

.. latex-toc-doxygenfunction:: ndigo_get_init_parameters

.. latex-toc-doxygenstruct:: ndigo_init_parameters

.. latex-toc-doxygenstruct:: ndigo_device