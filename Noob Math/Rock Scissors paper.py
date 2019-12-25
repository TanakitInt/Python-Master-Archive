"""This is docsrting"""
def main():
    """Docstring"""
    some_string = str(input())
    some_string2 = str(input())
    item = "RockScissorsPaper"
    if some_string in item and some_string2 in item:
        if some_string in "Rock" and some_string2 in "Rock":
            print("Banabana")
            print("Rock!!!")
        elif some_string == some_string2:
            print("Banabana")
        elif some_string in "Rock" and some_string2 in "Scissors":
            print("God of Banana")
            print("Rock!!!")
        elif some_string in "Rock" and some_string2 in "Paper":
            print("Banabird")
            print("Rock!!!")
        elif some_string in "Scissors" and some_string2 in "Paper":
            print("God of Banana")
        elif some_string in "Scissors" and some_string2 in "Rock":
            print("Banabird")
        elif some_string in "Paper" and some_string2 in "Rock":
            print("God of Banana")
        elif some_string in "Paper" and some_string2 in "Scissors":
            print("Banabird")
    else:
        print("")
main()
