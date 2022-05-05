#!/usr/bin/env python


class FormatVersion:
    """
    base iterator for processing a given format version
    """
    def __init__ (self, allRows):
        self.allRows = allRows
        self.rowptr = 0
        if allRows[0][0].upper() == 'DATE':
            raise RuntimeError("The first row is likely column headers. Try running again with the --header option")

    def __iter__ (self):
        return self

    def next (self):
        try:
            row = self.allRows[self.rowptr]     # pylint: unused-variable
        except IndexError:
            raise StopIteration

        self.rowptr += 1

        # insert version specific implementation here

        date = None
        ref = None
        payee = None
        customer = None
        amount = None
        memo = None

        result = (date, ref, payee, customer, amount, memo)
        return result


class FormatVersion0 (FormatVersion):
    """
    formerly the 'old' format
    # 01/29/2016  Fri,,"RESTAURANT","Card Holder Name","XXXX-XXXXXX-NNNNN",,,3.27,,,,,,,,
    # COLS:  0:Date, 1:Ref?, 2:Payee, 3:Card-holder-name, 4:Card-number, 5:memo, 7:Amount
    """

    def next (self):
        try:
            row = self.allRows[self.rowptr]
        except IndexError:
            raise StopIteration

        self.rowptr += 1

        date = row[0].split()[0]
        ref = None
        payee = row[2]
        customer = row[3].split()[0]
        try:
            amount = -float(row[7])
        except:
            raise RuntimeError("Error in amount (%s) in column 7 on line %d of CSV file" % (row[7], self.rowptr))
        memo = row[5]

        result = (date, ref, payee, customer, amount, memo)
        return result


class FormatVersion1 (FormatVersion):
    """
    formerly the 'new' format
    # 2/8/20,PANASONIC- EVA AIR,JONATHAN M CAMERON,-23011,14.95
    # COLS:  0:Date, 1:Payee, 2:Card-holder-name, 3:Card-number, 4:Amount
    """

    def next (self):
        try:
            row = self.allRows[self.rowptr]
        except IndexError:
            raise StopIteration

        self.rowptr += 1

        date = row[0]
        ref = None
        payee = row[1]
        customer = row[2]
        try:
            amount = -float(row[4])
        except:
            raise RuntimeError("Error in amount (%s) in column 5 on line %d of CSV file" % (row[4], self.rowptr))
        memo = None

        result = (date, ref, payee, customer, amount, memo)
        return result


class FormatVersion2 (FormatVersion):
    """
    formerly the 'new2' format
    # Transaction Date,Post Date,Description,Category,Type,Amount
    # COLS:  0:Date, 2:Description(payee), 3:Category(not useful), 4:type(not useful), 5:Amount
    """

    def next (self):
        try:
            row = self.allRows[self.rowptr]
        except IndexError:
            raise StopIteration

        self.rowptr += 1

        date = row[0]
        ref = None
        payee = row[2]
        customer = None
        try:
            amount = float(row[5])
        except:
            raise RuntimeError("Error in amount (%s) in last column on line %d of CSV file" % (row[5], self.rowptr))
        memo = None

        result = (date, ref, payee, customer, amount, memo)
        return result


class FormatVersion3 (FormatVersion):
    """
    formerly the 'default' format
    """

    def next (self):
        try:
            row = self.allRows[self.rowptr]
        except IndexError:
            raise StopIteration
        self.rowptr += 1

        date = row[0]
        ref = row[1].split()[1]
        amount = float(row[2])
        payee = row[3]
        memo = row[4]
        customer = None

        result = (date, ref, payee, customer, amount, memo)
        return result


class FormatVersion4 (FormatVersion):
    """
    another format as of file downloaded May 2022
    """

    def next (self):
        try:
            row = self.allRows[self.rowptr]
        except IndexError:
            raise StopIteration

        self.rowptr += 1

        date = row[0]
        amount = float(row[2])
        try:
            payee = row[3].split("\n")[1]
        except IndexError:
            payee = 'UNK_PAYEE'
        ref = row[9]
        memo = row[10]
        customer = None
        result = (date, ref, payee, customer, amount, memo)
        return result
