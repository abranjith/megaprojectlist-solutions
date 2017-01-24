__author__ = 'Ranjith'

def get_vowel_count(input_string):
    vowels_dict = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for c in input_string:
        if c.lower() in vowels_dict.keys():
            vowels_dict[c.lower()] += 1

    return vowels_dict


if __name__ == "__main__":

   input_string = raw_input("Enter a string : ")

   vowels_dict = get_vowel_count(input_string)

   print "Here is vowels summary from your list"
   print "*"*40

   for k, v in vowels_dict.items():
       print "%s  ---  %d" %(k, v)