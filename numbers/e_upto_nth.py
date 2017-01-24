__author__ = 'Ranjith'
import math
import sys
from decimal import Decimal

def fact(n):
    if n < 2:
        return 1
   # else:
   #     return n * fact(n-1)

    factr = 1
    for i in xrange(1, n+1):
        factr *= i

    return factr


def mw_e_ndigits(n):

    e_val = 1

    for i in xrange(1, 1001):
        e_val += 1/Decimal(fact(i))

    format_as = "."+str(n+1)+"g"
    return format(e_val, format_as)

def ew_e_ndigits(n):

    if n < 1:
        return 2

    format_as = "."+str(n+1)+"g"
    return format(math.e, format_as)

if __name__ == "__main__":

    print sys.argv
    if len(sys.argv) > 1:
        num_of_digits = sys.argv[1]
    else:
        num_of_digits = int(raw_input("Enter number of digits : ").strip())

    assert(isinstance(num_of_digits, int)), "Number of digits provided is not an integer"
    assert(num_of_digits<101), "Number of digits cannot be greater than 100"

    print ew_e_ndigits(num_of_digits)
    print mw_e_ndigits(num_of_digits)
