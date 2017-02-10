from math import *
from turtle import *

cmds = ["say", "draw", "info", "calculate", "help", "quiz", "newcommand", "name", "company"]
name = input("What's your name? ")

def command():
      question = input("%s> " % name)

      if question == cmds[0].casefold():
          say()

      elif question == cmds[1].casefold():
          draw()

      elif question == cmds[2].casefold():
          print("This is AlessioScript, a programming language by Alessio.")
          command()

      elif question == cmds[3].casefold():
          calculate()

      elif question == cmds[4].casefold():
          print("That's the commands I know:")
          print(cmds)
          command()

      elif question == cmds[5].casefold():
          quiz()

      elif question == cmds[6].casefold():
          command()

      elif question == cmds[7].casefold():
          print("Your name is %s! " % name)

      elif question == cmds[8].casefold():
            print("Check out Alessio's company:")
            print("https://zoniklalessimo.000webhostapp.com")
            command()
                            
      else:
            print("I don't know this command. ")
            command()
          
def say():
     speech = input("What do you wan't me to say? ")
     print(speech)
     command()

def quiz():
     points = 0
     questions = ["Who's the inventor of AlessioScript? ",
                           "In which programming language has AlessioScript been written? ",
                           "Which river passes Prague? ",
                           "What does 'amazing' mean in german? "]
     answers = ["Alessio",
                        "Python",
                        "Moldova",
                        "Fantastisch"]

     for question, answer in zip(questions,answers):
          if input(question).casefold() == answer.casefold():
               points += 1
               if points > 1:
                    print("Perfect! You now have %s points!" % points)
               else:
                    print("Perfect! You now have %s point!" % points)
          else:
               print("Wrong! %s would have been right!" % answer)
     if points >= 2:
          print("Great, your score is %s points + 1 participation point! " % points)
     elif points == 1:
          print("Not bad, your score is %s point + 1 participation point! " % points)
     elif points == 0:
          print("At least you have 1 participation point... ")
     command()

def draw():
     speed(4)
     drawing = input("draw> ")
     if drawing == "House".casefold():
          draw_house()
     elif drawing == "Soersel".casefold():
          draw_circle()
     elif drawing == "Square".casefold():
          draw_square()
     elif drawing == cmds[6].casefold():
          command()
     else:
          print("I can't draw this!")
          draw()
     
def draw_house():
     a = 200
     lt(90)
     fd(a)
     rt(90)
     fd(a)
     lt(135)
     fd(a/sqrt(2))
     lt(90)
     fd(a/sqrt(2))
     lt(90)
     fd(sqrt(2)*a)
     lt(135)
     fd(a)
     lt(135)
     fd(sqrt(2)*a)
     lt(135)
     fd(a)
     command()

def draw_circle():
     a = 200
     circle(a*0,5)
     command()

def draw_square():
     a = 200
     for i in range(4):
          fd(a)
          lt(90)
     command()

def calculate():
     x = int(input("Enter your first number "))
     y = int(input("Enter your second number "))
     opt = input("Enter an operator (+, -, *, /, sqrt) ")
     if opt == "+":
          print(x, " + ", y, " = ", x + y)
     elif opt == "-":
          print(x, " - ", y, " = ", x - y)
     elif opt == "*":
          print(x, " * ", y, " = ", x * y)
     elif opt == "/":
          print(x, " + ", y, " = ", x / y)
     elif opt == "sqrt":
          print("The squareroot of ", x, "is", sqrt(x), "and the squareroot of ", y, "is", sqrt(y), "! ")
     elif opt == cmds[6].casefold():
         command()
     command()
          
command()
input()

