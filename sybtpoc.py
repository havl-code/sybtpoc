# import module and library
import random
from tabulate import tabulate


# welcome user and ask for user choice of function
def welcome():
    print("=========================================")
    print("Welcom to SYBTPOC!")
    print("Should You Buy This Piece of Clothing?")
    print("-----------------------------------------")
    print("Choose what you want to do: ")
    print("1: How does this work?")
    print("2: Let's try this out!")

    # check if user input is a number or not
    try:
        userChoice = int(input("> "))
    except:
        print("Please type [1] or [2]!")
        welcome()
        return

    # check user choice and proceed to start the desired function
    if userChoice == 1:
        about()
    elif userChoice == 2:
        ask()
    # if user choice is not 1 or 2, ask for user choice again
    elif userChoice != 1 and userChoice != 2:
        print("Please type [1] or [2]!")
        welcome()


# function 1
def about():
    print("=========================================")

    # create a list of sentences
    table = [["10 questions will be shown."], ["You need to answer each question by typing in [Y] (YES) or [N] (NO)."],
             ["Your item grade will be graded based on your answers."], 
             ["If your item's grade is greater than or equal to 50 scores, you should buy this piece of clothing."],
             ["Otherwise, you should not buy it."], ["Have a nice experience using this program!"]]
    header = ["How does this work?"]

    # create a table of instruction
    print(tabulate(table, header, tablefmt="psql", stralign="left"))

    # call def goodbye()
    goodbye()


# function 2
def ask():
    print("=========================================")

    #user input the item's name
    print("What is this piece of clothing that you are considering buying? (e.g., skirt)")
    userItem = str(input("> ")).capitalize()

    #list of questions
    questionsList = ['Does it fit your style concept?', 'Do you like the fit and fabric?', 'Can you think of at least 3 outfits to wear it with?',
                     'Is this item comfortable?', 'Was this made responsibly?', 'Is this something you truly love?', 'Will you want to wear this next year?',
                     'Will this go with other pieces in your wardrobe?', 'You are not buying this just because it is on sale, right?',
                     'You are not buying this for external validation, right?']

    itemGrade = 0
    questionPos = 0

    randomQuestions = random.sample(questionsList, len(questionsList))

    #interation
    for q in range(len(randomQuestions)):
        print("-----------------------------------------")
        q = randomQuestions[questionPos]
        print(q)
        userAns = str(input("> ")).upper()

        #check if user item is valid or not
        while userAns not in ['Y', 'N']:
            print("Please type [Y] or [N]")
            userAns = str(input("> ")).upper()

        #selection
        if userAns == "Y":
            itemGrade += 10
        elif userAns == "N":
            itemGrade += 0

        questionPos += 1

    result(userItem, itemGrade)

def result(userItem, itemGrade):

    # print result and recommendation
    print("_________________________________________")
    print(userItem, "got", itemGrade, "scores")

    if itemGrade >= 80:
        print("You should buy", userItem,
              ",you are going to look stunning in it!")
    elif itemGrade >= 50:
        print("You may buy", userItem,
              ", but check if there is any better option first.")
    else:
        print("You should not buy", userItem,
              ",save your money for a better item.")

    # call def goodbye()
    goodbye()


# ask if user want to continue using program or not
def goodbye():

    # ask question
    print("=========================================")
    print("Do you want to continue using this program? [Y] or [N]")

    # check if user's input is valid or not
    try:
        userCont = str(input("> ")).upper()
    except:
        print("Please type [Y] or [N]!")
        goodbye()
        return

    # decide what to do based on user input
    if userCont == "Y":
        welcome()
    elif userCont == "N":
        print("-----------------------------------------")
        print("Thank You for Using SYBTPOC!")
    elif userCont != "Y" and userCont != "N":
        print("Please type [Y] or [N]!")
        goodbye()


# call welcome() to start the program
welcome()
