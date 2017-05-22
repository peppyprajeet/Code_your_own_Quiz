# IPND Stage 2 Final Project

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#-----------#
#-Questions-#
#-----------#

#Prompt Question
questions = ["""What should be filled in for __1__?""",
             """What should be filled in for __2__?""",
             """What should be filled in for __3__?""",
             """What should be filled in for __4__?"""]

holders = ['__1__','__2__','__3__','__4__']

#Quiz Templates
quiz_text = {'easy':"""***The current paragraph reads as such***

Programming Language starts with basic output, 'Hello __1__!'

In __2__ this is easy;

Syntax for this is: __3__ 'Hello __1__!'

A__4__is created with def keyword.""",


'medium':"""***The current paragraph reads as such***

A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.""",

'hard':"""***The current paragraph reads as such***

Artificial __1__ (A.I.)has become a 'buzz word' of publications everywhere.

However to better understand A.I. we'll dive into two topics.
The first is Computer __2__ (CV) which allows a computer to 'see'
and label what's in the computers surroundings. The second is
Natural __3__ Processing (NLP) which allows computers to understand
voice commands as well as speak back to the user.

All of this is now becoming possible due to Deep __4__ (DL)
and Machine __4__ (ML).
"""}

#---Answers to Quizes---#
answers = {'easy':['World','python','print','function'],
           'medium':['function','arguments','None','list'],
           'hard':['Intelligence','Vision','Language','Learning']}

choices = []

#-----------#
#-Functions-#
#-----------#

def win(guesses):
    #---Function if Player Wins the Game---#
    #Input: Number of tries remaining
    #Output: The you won the game message
    winning = "***You won with " + str(guesses) + " guesses remaining!***"
    return winning

def right(choice_index,level,guesses):
    #---Function if Player Chooses Right---#
    #Inputs: Which answer user is on, level, and number of tries remaining
    #Outputs: Choice function with a reduced number of tries remaining
    correct_answer = """
***Correct! '""" + str(choices[choice_index]) + "' is the right choice!***"
    print correct_answer
    quiz_text[level] = quiz_text[level].replace(holders[choice_index],choices[choice_index])
    return choice(level,choice_index+1,guesses)

def wrong(guesses,level,choice_index):
    #---Function if Player Chooses Wrong---#
    #Inputs: Number of tries remaining, level, and which answer user is on
    #Outputs: Game Over Message, or Wrong Answer Message
    wrong_choice = choices.pop()
    if guesses == 0:
        game_over = "***You've chosen wrong too many times!  Game over!****"
        return game_over
    else:
        guesses -= 1
        wrong_answer_text = """***'""" + wrong_choice + """' isn't the correct answer!***
***Let's try again; you have """ + str(guesses) + ' trys left!***'
        print wrong_answer_text
        return choice(level,choice_index,guesses)

def choice(level,choice_index,guesses):
    #---Function to Prompt User for an Answer---#
    #Inputs: level, which question the user is on, and how many tries remain
    #Outputs: Winning Message, Correct Answer Message, Wrong Answer Message, or Game Over Message
    print quiz_text[level]
    if choice_index == len(answers[level]):
        return win(guesses)
    choices.append(raw_input(questions[choice_index]))
    if choices[choice_index] == answers[level][choice_index]:
        return right(choice_index,level,guesses)
    else:
        return wrong(guesses,level,choice_index)

def start(level):
    guesses_prompt = """***Please select the number of guesses you'd like***"""
    guesses = raw_input(guesses_prompt)
    if int(guesses):
        guesses = int(guesses)
        guess_text = """
***You will get '""" + str(guesses) + " trys!***"
        print guess_text
        return choice(level.lower(),0,guesses)


def quiz():
    #---Overarching Quiz Function---#
    user_prompt = """
***Please select a game difficulty by typing it in!***
***Possible choices include easy, medium, and hard***
"""
    level = raw_input(user_prompt)
    intro = """
***You've chosen """ + str(level) + "!***"
    print intro
    if level.lower() == 'hard' or level.lower() == 'medium' or level.lower() == 'easy':
        return start(level)
    else:
        wrong_level = """
***'""" + level + "' is not a level option!***"
        print wrong_level
        return quiz()

#-----------------#
#-Running Program-#
#-----------------#
print quiz()
