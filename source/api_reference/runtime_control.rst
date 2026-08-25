.. raw:: latex

    \clearpage

===============
Runtime Control
===============

Once an Ndigo5G device is configured, the following functions can be used to
control the behavior of it.

These functions return quickly with very little overhead. However, they are not
guaranteed to be thread safe. 

.. latex-toc-doxygenfunction:: ndigo_start_capture

.. latex-toc-doxygenfunction:: ndigo_stop_capture

.. latex-toc-doxygenfunction:: ndigo_pause_capture

.. latex-toc-doxygenfunction:: ndigo_continue_capture

.. latex-toc-doxygenfunction:: ndigo_single_shot

.. latex-toc-doxygenfunction:: ndigo_manual_trigger
