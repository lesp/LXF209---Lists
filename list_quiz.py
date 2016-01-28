import easygui as eg
from random import randint

questions = ["What berry fruit is also the name of a computer?",
             "What programming language sounds like a snake?",
             "What programming language sounds like a precious stone?",
             "What is the name of the Raspberry Pi operating system?"]

answer = ["raspberry","python","ruby","raspbian"]


for question in range(len(questions)):
    item = randint(0,3)
    response = eg.enterbox(msg=questions[item],title="Question")

    if response == answer[item]:
        eg.msgbox(msg="Correct")
    else:
        eg.msgbox(msg="Incorrect")
