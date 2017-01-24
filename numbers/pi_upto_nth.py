__author__ = 'Ranjith'
import math
import sys

def mw_pi_ndigits(n):
    str_pi, remindr = str(22/7), 22%7

    if n<1:
        return str_pi

    str_pi += "."

    for i in xrange(n):
        div, remindr = (remindr*10)/7, (remindr*10)%7
        str_pi += str(div)

    return str_pi

def ew_pi_ndigits(n):

    if n<1:
        return 3

    format_as = "."+str(n+1)+"g"
    return format(math.pi, format_as)

if __name__ == "__main__":

    print sys.argv
    if len(sys.argv) > 1:
        num_of_digits = sys.argv[1]
    else:
        num_of_digits = int(raw_input("Enter number of digits : ").strip())

    assert(isinstance(num_of_digits, int)), "Number of digits provided is not an integer"
    assert(num_of_digits<101), "Number of digits cannot be greater than 100"

    print ew_pi_ndigits(num_of_digits)
    print mw_pi_ndigits(num_of_digits)
