__author__ = 'Ranjith'
import sys

def fib_ndigits(n):

    a, b = 0, 1

    for i in xrange(n):
        yield a
        a, b = b, a+b

if __name__ == "__main__":

    if len(sys.argv) > 1:
        num_of_digits = sys.argv[1]
    else:
        num_of_digits = int(raw_input("Enter n to generate fibonacci upto nth : ").strip())

    assert(isinstance(num_of_digits, int)), "Number provided is not an integer"
    assert(num_of_digits < 100001), "Number cannot be greater than 100000"

    for i in fib_ndigits(num_of_digits):
        print i
