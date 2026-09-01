===============================
Auto Trigger Function Generator
===============================


Some applications require periodic or random triggering.
Ndigo5G’s function generator provides this functionality.


The delay between two trigger pulses of this trigger generator is the
sum of two components:

A fixed value :math:`M` and a pseudo random value
given by the exponent :math:`N`.


The period is


.. math::

    T = M + [1...2^N] - 1


clock cycles with a duration of 3.2 ns per cycle, where
:math:`8 \leq M < 2^{32}` and :math:`0 \leq N < 32`.



This allows to monitor input signals at times the current trigger
configuration does not trigger, e.g., to get baseline information in
mass spectrometry applications.


It can also be used to determine a suitable threshold level for the trigger
by first getting random statistics on the input signal.
