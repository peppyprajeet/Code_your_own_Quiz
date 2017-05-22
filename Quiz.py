# -*- coding: cp1252 -*-
# IPND Stage 2 Final Project

#Questions
questions = ["""What should be filled in for __1__?""",
             """What should be filled in for __2__?""",
             """What should be filled in for __3__?""",
             """What should be filled in for __4__?"""]

holders = ['__1__','__2__','__3__','__4__']

#Quiz Templates
quiz_text = {'easy':"""***Read the Paragraph and Fill in the blanks as needed***

Programming Language starts with basic output, 'Hello __1__!'
In __2__ this is easy;
Syntax for this is: __3__ 'Hello __1__!'
In __2__ a function is created with __4__ keyword.""",


'medium':"""***Read the Paragraph and Fill in the blanks as needed***

A __1__ is created with the def keyword.
You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.""",

'hard':"""***Read the Paragraph and Fill in the blanks as needed***

Machine learning is the subfield of computer science that, according to Arthur Samuel in 1959,
gives "computers the ability to learn without being explicitly programmed."

Evolved from the study of __1__ recognition and computational learning theory in artificial intelligence,
machine learning explores the study and construction of __2__ that can learn from and make predictions
on data – such __2__ overcome following strictly static program instructions by making data-driven predictions or decisions,
through building a model from sample inputs.

Machine learning is employed in a range of computing tasks where designing and programming
explicit __2__ with good performance is difficult or unfeasible;example applications include email filtering,
detection of network intruders or __3__ insiders working towards a data breach,__4__ character recognition (OCR),learning to rank and computer vision.
"""}

#Answers to Quizes
answers = {'easy':['World','python','print','def'],
           'medium':['function','arguments','None','list'],
           'hard':['pattern','algorithms','malicious','optical']}

choices = []

#Functions
def win(guesses):

    #If Player Wins the Game
    winning = " You won with " + str(guesses) + " guesses remaining! "
    return winning

def right(choice_index,level,guesses):

    #If Player Chooses Right
    correct_answer = """ Correct! '""" + str(choices[choice_index]) + "' is the right choice! "
    print correct_answer
    quiz_text[level] = quiz_text[level].replace(holders[choice_index],choices[choice_index])
    return choice(level,choice_index+1,guesses)

def wrong(guesses,level,choice_index):

    #If Player Chooses Wrong
    wrong_choice = choices.pop()
    if guesses == 0:
        game_over = " You've chosen wrong too many times! Game over! "
        return game_over
    else:
        guesses -= 1
        wrong_answer_text = """ '""" + wrong_choice + """' isn't the correct answer!
Try again; you have """ + str(guesses) + ' trys left!'

        print wrong_answer_text
        return choice(level,choice_index,guesses)

def choice(level,choice_index,guesses):

    #Prompt User for an Answer
    print quiz_text[level]
    if choice_index == len(answers[level]):
        return win(guesses)
    choices.append(raw_input(questions[choice_index]))
    if choices[choice_index] == answers[level][choice_index]:
        return right(choice_index,level,guesses)
    else:
        return wrong(guesses,level,choice_index)

def start(level):

    #Choosing guesses according to level
    guesses_prompt = """ Please select the number of guesses you'd like """
    guesses = raw_input(guesses_prompt)
    if int(guesses):
        guesses = int(guesses)
        guess_text = """ You will get '""" + str(guesses) + " trys! "
        print guess_text
        return choice(level.lower(),0,guesses)


def quiz():

    #Quiz Function
    user_prompt = """ Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard """
    level = raw_input(user_prompt)
    intro = """ You've chosen """ + str(level) + "!"
    print intro
    if level.lower() == 'hard' or level.lower() == 'medium' or level.lower() == 'easy':
        return start(level)
    else:
        wrong_level = """ '""" + level + "' is not a level option! "
        print wrong_level
        return quiz()

print quiz()
