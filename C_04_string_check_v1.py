# Functions goes here
def string_check(question, valid_ans_list):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

    # main routine goes here


levels = ['easy', 'medium', 'hard']

like_coffe = string_check("Do you like coffe?", ['yes', 'no'])
print(f"You chose {like_coffe}")
choose_levels = string_check("choose a level", levels)
print(f"You chose {choose_levels}")
