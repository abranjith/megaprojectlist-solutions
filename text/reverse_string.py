__author__ = 'Ranjith'

if __name__ == "__main__":

   input_string = raw_input("Enter a string to reverse : ")

   reverse_string_1 = input_string[::-1]

   reverse_string_2 = ''
   for i in xrange(len(input_string)-1, -1, -1):
       reverse_string_2 += input_string[i]

   print "Reversed string : %s" %(reverse_string_1)
   print "Reversed string : %s" %(reverse_string_2)