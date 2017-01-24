__author__ = 'Ranjith'
import sys

def is_prime(num):
    for i in xrange(2, (num+2)/2):
        if num % i == 0:
            return False

    return True

def prime_gen():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

if __name__ == "__main__":

    a = prime_gen()

    while True:
        yes_no = str(raw_input("Continue generating prime numbers (Y/N) ? : ").strip())

        if yes_no.lower() == "y":
            print  a.next()
        else:
            print "OK.. Byeeeee"
            break