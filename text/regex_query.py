__author__ = 'Ranjith'
import re

def pattern_matcher(string, pattern):

    #Compile
    compiled_re = re.compile(pattern)

    match_list = compiled_re.findall(string)

    return match_list[:]

if __name__ == "__main__":

   input_string = raw_input("Enter a string : ")
   input_pattern = raw_input("Enter pattern to match : ")

   matched_data = pattern_matcher(input_string, input_pattern)

   if len(matched_data) > 0:
       print "Below are the matched strings"
       print "*"*30
       for data in matched_data:
           if data:
               print data

   else:
       print "Nothing matches!"