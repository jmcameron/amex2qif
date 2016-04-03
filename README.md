amex2qif
========

Convert American Express CSV export files to QIF format.

Several years ago, American Express dropped support for the QIF format for
exporting statements.  However, American Express still supports exporting data
in Comma Separated Value file (CSV) format.   This software allows you to
conver the CSV statement into a QIF file on your local computer.

USAGE: 

    amex2qif statement.csv > statement.qif

where 'statement.csv' is a CSV statement downloaded from American Express.

This will create the file 'statement.qif' from the CSV 

If you provide a 'categories.txt' file in the same directory as the amex2qif
program, it will automatically be used.  Each line should have the vendor
name, a comman, and then the category to be used when the payee matches that
vendor.  Empty lines are ignored.  A default version of this file can be kept
in the directory of the amex2qif executable.  If a copy of this file is found
in the directory that this ommand is run in, it overrides the version in the
executable directory.