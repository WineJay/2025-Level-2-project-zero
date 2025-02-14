# Functions goes here
def num_check(question, num_type, exit_code=None):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float
    while True:

        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purposes...
while True:
    print()

    my_float = num_check("Please enter a number more than 0: ", "float")
    print(f"Thanks. you chose {my_float}")

    my_int = num_check("How many rounds? ", "integer", "")
    print()
    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")
