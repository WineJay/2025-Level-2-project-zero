# Functions goes here
def int_check(question):
    """checks that the user enter an integer. """

    error = "Oops - please enter an integer. "

    while True:
        try:
            # Return the response if it's an integer
            response = int(input(question))
            return response

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function!
    # ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    else:
        print(f"{name} brought a ticket")
