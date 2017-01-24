__author__ = 'Ranjith'
import sys

def is_prime(num):
    for k in xrange(2, (num+2)/2):
        if num % k == 0:
            return False

    return True

def prime_factors(n):

    for i in xrange(2, n+1):
        if n % i == 0 and is_prime(i):
            yield i

if __name__ == "__main__":

    if len(sys.argv) > 1:
        num_of_digits = sys.argv[1]
    else:
        num_of_digits = int(raw_input("Enter a number to know its prime factors : ").strip())

    assert(isinstance(num_of_digits, int)), "Number provided is not an integer"
    assert(num_of_digits < 1000001), "Number cannot be greater than 1000000"

    for j in prime_factors(num_of_digits):
        print j
