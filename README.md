amex2qif
========

Convert American Express CSV export files to QIF format.

Several years ago, American Express dropped support for the QIF format for
exporting statements.  However, American Express still supports exporting data
in Comma Separated Value file (CSV) format.   This software allows you to
convert the CSV statement into a QIF file on your local computer.

Usage
-----

Here is how to run this program:

    amex2qif statement.csv > statement.qif

where 'statement.csv' is a CSV statement downloaded from American Express.

This will create the file 'statement.qif' from the CSV file 'statement.csv'.

The program supports several options. Do:

    amex2qif --help
   
to see the supported options


Format of CSV files
-------------------

The program supports two formats of CSV files from AMEX: Old-style, and
New-style.  It seems like recent imports (circa 2017) are using old-style
again. 

In the old-style, the columns are:

    1:Date, 2:Ref?, 3:Payee, 4:Card-holder-name, 5:Card-number, 8:Amount

It is unclear what AMEX expects to be in columns 6 and 7.

There is no memo in the old-style CSV files from AMEX.  However if you edit
the CSV file before coverting to a QIF file, insert a memo in column 6 and the
it will be added to the memo field in the QIF output for that item.

In the new-style, the columns are:

    1:Data, 2:Reference, 3:Amount, 4:Payee, 5:Memo


Automatic Categorization
------------------------

If you provide a 'categories.txt' file in the same directory in which you
execute the **amex2qif** program or in direcotry containing the **amex2qif**
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
