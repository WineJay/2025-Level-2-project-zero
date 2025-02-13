# Functions goes here
def string_check(question, valid_ans_list, num_letters):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

    # main routine goes here


yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffe = string_check("Do you like coffe?",
                          yes_no_list, 1)
print(f"You chose {like_coffe}")
pay_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")
