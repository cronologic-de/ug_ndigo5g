=================
Data Lookup Table
=================


In some applications it might be useful to modify the ADC sample data by
a user defined function *f*\ (*x*\ ).


In this case, the onboard FPGA is able to perform this task such that the
data stream consists of data words *f*\ (*sample*\ ) instead of
*sample*.


The function *f*\ (*x*\ ) is applied using a 1024 word lookup table (LUT)
which needs to be provided by the user.


This is done by defining the corresponding function using
:member:`ndigo_configuration::custom_lut`.


Please feel free to contact cronologic if you plan the use this feature.


The onboard INL correction is applied prior to mapping the LUT values.