# Functions goes here
def int_check(question, num_type, exit_code=None):
    """checks that the user enter an integer. """

    error + "Oops - please enter an integer. "

    while True:

        try:
            # Return the response if it's an integer
            int(input(question))

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function!
    # ask for their age and check if it's between 12 and 120
    int_check("Age: ")
