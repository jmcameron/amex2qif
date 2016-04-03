amex2qif
========

Convert American Express CSV export files to QIF format.

Several years ago, American Express dropped support for the QIF format for
exporting statements.  However, American Express still supports exporting data
in Comma Separated Value file (CSV) format.   This software allows you to
conver the CSV statement into a QIF file on your local computer.

Usage
-----

Here is how to run this program:

    amex2qif statement.csv > statement.qif

where 'statement.csv' is a CSV statement downloaded from American Express.

This will create the file 'statement.qif' from the CSV 

Automatic Categorization
------------------------

If you provide a 'categories.txt' file in the same directory as the **amex2qif**
program, it will used to automatically assign categories to transactions if
the payee matches know vendors.  

**Format of 'categories.txt'**

Each line should have the vendor name, a comma, and then the category
to be used when the payee matches that vendor.  Empty lines are ignored.  A
default version of this file can be kept in the directory of the **amex2qif**
executable.  If a copy of this file is found in the directory that this ommand
is run in, it overrides the version in the executable directory.

Running on Windows
------------------

TBD... First you must install Python on your windows system.

Disclaimer
----------

This work is not connected to American Express or sponsored by it in any way!

-Jonathan Cameron
 jmcameron@gmail.com
