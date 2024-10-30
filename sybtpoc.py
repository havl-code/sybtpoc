# import required modules
import random
from tabulate import tabulate


# display welcome message and prompt user to choose an option
def welcome():
    print("=" * 40)
    print("Welcom to SYBTPOC!")
    print("Should You Buy This Piece of Clothing?")
    print("-" * 40)
    print("Choose what you want to do: ")
    print("1: How does this work?")
    print("2: Let's try this out!")

    # loop to validate and handle user input
    while True:
        try:
            user_choice = int(input("> "))
            if user_choice == 1:
                about() # show how the program works
                break
            elif user_choice == 2:
                ask()   # start the decision-making questions
                break
            else:
                print("Please type [1] or [2]!")
        except ValueError:
            print("Please type [1] or [2]!")

# function 1: explain how the program works, display scoring table
def about():
    print("=" * 40)
    print("How does this work?")
    print("=" * 40)

    # instructions for the user
    guide = [
        "1. You will be shown 10 questions.",
        "2. Answer each question with [Y] (YES) or [N] (NO).",
        "3. Your item's grade will be calculated based on your answers.",
        "4. If the grade is 50 or above, you may consider buying it!",
        "Enjoy using this program!"
    ]
    print("\n".join(guide))

    # define and display the scoring table with advice
    header = ["Score", "Advice"]
    table = [["0 < item's grade < 50", "You should not buy this item, save your money for a better item."],
             ["50 <= item's grade < 80",
                 "You may buy this item but check if there is any better option first."],
             ["80 < item's grade <= 100", "You should definitely buy this item!"]]

    # print scoreboard
    print("\n" + tabulate(table, header, tablefmt="grid", stralign="center"))

    goodbye()

# function 2: prompt the user to answer questions about the item and calculate a grade
def ask():
    print("=" * 40)

    # get the name of the item the user is considering buying
    userItem = input("What item are you considering buying? (e.g., skirt): ").capitalize()

    # list of questions for the user
    questionsList = [
        "Does it fit your style concept?", 
        "Do you like the fit and fabric?", 
        "Can you think of at least 3 outfits to wear it with?", 
        "Is this item comfortable?", 
        "Was this made responsibly?", 
        "Is this something you truly love?", 
        "Will you want to wear this next year?", 
        "Will this go with other pieces in your wardrobe?", 
        "You are not buying this just because it is on sale, right?", 
        "You are not buying this for external validation, right?"
    ]

    itemGrade = 0   # initialise the item grade score

    # ask each question in a randomized order and calculate the score based on answers
    for q in random.sample(questionsList, len(questionsList)):
        print("-" * 40)
        print(f"{q} (Y/N)")

        # validate user input for each question
        while True:
            userAns = input("> ").strip().upper()
            if userAns in ['Y', 'N']:
                itemGrade += 10 if userAns == 'Y' else 0
                break
            else:
                print("Please type [Y] or [N]")

    # display the final result based on the score
    print("=" * 40)
    print("Thank you for your answers! Here is the result:")
    result(userItem, itemGrade)

# display the item score and provide purchase advice based on the grade
def result(userItem, itemGrade):
    # print result and recommendation
    print("_" * 40)
    print(f"{userItem} scored {itemGrade} points.")

    # provide recommendation based on the score range
    if itemGrade >= 80:
        print(f"You should buy {userItem}! You're going to look stunning in it!")
    elif itemGrade >= 50:
        print(f"You may buy {userItem}, but check if there is any better option first.")
    else:
        print(f"You should not buy {userItem},save your money for a better item.")

    goodbye()


# ask if user want to continue using program
def goodbye(): 
    # ask question
    print("=" * 40)
    print("Do you want to continue using this program? (Y/N)")

    # loop to validate and handle user choice
    while True:
        userCont = input("> ").strip().upper()
        if userCont == "Y":
            welcome()
            break
        elif userCont == "N":
            print("-" * 40)
            print("Thank you for using SYBTPOC!")
            break
        else:
            print("Please type [Y] or [N]")


# start the program by calling the welcome function
welcome()