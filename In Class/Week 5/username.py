# username.py
# Simple string processing program to generate usernames: 
# First initial + first seven characters of last name

def main():
    print("This program generates computer usernames.\n")

    # get user's first and last names
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0].upper() + last[:7].lower()

    # output the username
    print("Your username is:", uname)

main()
