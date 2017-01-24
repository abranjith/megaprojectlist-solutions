__author__ = 'Ranjith'

def interest_per_month(total_loan, total_years, apr):

    total_interest_amount = 0
    monthly_principal_amount = total_loan / (total_years*12)

    for i in range(1, total_years*12+1):
        total_interest_amount += total_loan*(apr/100)/12
        total_loan -= monthly_principal_amount

    return total_interest_amount


if __name__ == "__main__":

   total_mortgage_amount = float(raw_input("Enter total mortgage amount : ").strip())
   total_mortgage_years = int(raw_input("Enter number of years : ").strip())
   mortgage_interest_rate = float(raw_input("Enter interest rate in percentage : ").strip())
   compounding_interval = str(raw_input("Enter compounding interval (M/ W/ D/ C : ").strip()).lower()

   totalamount_with_interest = total_mortgage_amount + interest_per_month(total_mortgage_amount, total_mortgage_years, mortgage_interest_rate)
   monthly_payment = totalamount_with_interest / total_mortgage_years / 12

   print "Your monthly payment : %.2f" %monthly_payment