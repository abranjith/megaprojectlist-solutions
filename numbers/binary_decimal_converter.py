__author__ = 'Ranjith'

def binary_to_deci(num):
    num = str(num)[::-1]

    dec_num = 0

    for i, n in enumerate(num):
        dec_num += int(n)*(2**i)

    return dec_num

def deci_to_binary(num):

    bin_str = ''

    while True:
        d, r = num / 2, num % 2
        bin_str += str(r)

        if d < 2:
            bin_str += str(d)
            break

        num = d

    return int(bin_str[::-1])

if __name__ == "__main__":

   while True:
        user_option = str(raw_input("Enter your option : ").strip())

        if user_option.lower() == "1":
            binary_num = int(raw_input("Enter binary number : ").strip())
            print "Decimal equivalent : %d" %(binary_to_deci(binary_num))
        elif user_option.lower() == "2":
            deci_num = int(raw_input("Enter decimal number : ").strip())
            print "Binary equivalent : %d" %(deci_to_binary(deci_num))
        else:
            print "OK.. Byeeeee"
            break