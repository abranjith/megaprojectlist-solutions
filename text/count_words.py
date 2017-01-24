__author__ = 'Ranjith'

if __name__ == "__main__":

   input_string = raw_input("Enter a string : ")

   words_in_string = []

   for word in input_string.split(' '):
       for wo in word.strip().split('\n'):
           for w in wo.strip().split('.'):
               if w.strip():
                   words_in_string.append(w)

   #print words_in_string
   print "Words in string : %d" %(len(words_in_string))
