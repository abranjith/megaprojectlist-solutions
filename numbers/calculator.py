__author__ = 'Ranjith'
import math

def get_input_data():
    numbers_to_proc = raw_input("Enter the numbers separated by comma) : ").strip().split(",")
    numbers_to_procli = [float(n.strip()) for n in numbers_to_proc]
    return numbers_to_procli[:]


if __name__ == "__main__":

    while True:

        print """ C*A*L*C*U*L*A*T*O*R\n+++++++++++++++++++++\n
\t1. Addition(+)\n
\t2. Subtraction(-)\n
\t3. Multiplication(*)\n
\t4. Division(/)\n
\t5. Mod(%)\n
\t6. Power(^)\n
\t7. Square root\n
       """

        user_choice = int(raw_input("Please enter your choice (numbers) : ").strip())

        if user_choice not in [1, 2, 3, 4, 5, 6, 7]:
            print "Invalid choice ...try again\n"
            continue

        numlist_to_process = get_input_data()
        #print numlist_to_process

        if user_choice == 1:
            result = reduce(lambda x, y : x + y, numlist_to_process)

        elif user_choice == 2:
            result = reduce(lambda x, y : x - y, numlist_to_process)

        elif user_choice == 3:
            result = reduce(lambda x, y: x * y, numlist_to_process)

        elif user_choice == 4:
            result = reduce(lambda x, y: x / y, numlist_to_process)

        elif user_choice == 5:
            numlist_to_process = [int(n) for n in numlist_to_process]
            result = reduce(lambda x, y: x % y, numlist_to_process)

        elif user_choice == 6:
            result = reduce(lambda x, y: x ** y, numlist_to_process)

        elif user_choice == 7:
            result_tmp = [math.sqrt(n) for n in numlist_to_process]
            result = ",".join(str(n) for n in result_tmp)

        print "Output = %s\n" %str(result)

        user_input = raw_input("Open calculator again? (Y/N) : ").strip()
        if user_input.lower() == "y":
            continue
        else:
            break
