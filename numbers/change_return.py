__author__ = 'Ranjith'
from collections import OrderedDict

def calculate_change(amount):
    amount = int(amount * 100)   #in cents

    quats, change = amount / 25, amount % 25
    dime, change = change / 10, change % 10
    nickel, change = change / 5, change % 5

    all_change = OrderedDict([("Quarters" , quats), ("Dime" , dime), ("Nickel" , nickel), ("Cents" , change)])

    return all_change

if __name__ == "__main__":

   cost = float(raw_input("Enter the cost of purchase : ").strip())
   given_amount = float(raw_input("Enter the given amount : ").strip())

   if cost > given_amount:
       print "You owe us ... :@"
   else:
       change_amount =  given_amount - cost
       change_amount = float("{0:.2f}".format(change_amount))

       get_change = calculate_change(change_amount)

       print "Here is your change :"
       print "#"*30

       for k in get_change.keys():
               print k , " : " , get_change.get(k,0)

       print "#"*30

   print "Thank you !"
