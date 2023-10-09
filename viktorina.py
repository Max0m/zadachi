import time


print("Weolcome to  the science quiz!")
print("You have 5 questions to answer.")
score = 0


print("What is the smallest planet in the Solar System?")
one = input()
if one == "Mercury" or one == "mercury":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Mercury.")
print()
print()
print("Botany is the study of _______ ?")
two = input()
if two == "plants" or two == "Plants":
    score = score + 1
    print("Correct!")
    print
else:
    print("Incorrect.")
    print("The correct answer is plants.")
print()
print()
print("How many wings does a bee have?")
three = input()
if three == "2" or three == "two" or three == "Two":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is two.")
print()
print()
print("What is the name of the largest ocean on earth?")
four = input()
if four == "Pacific" or four == "pacific":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Pacific.")
print()
print()
print("Calculate: 2+3*2")
five = input()
if five == "8" or five == "eight" or five == "Eight":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is 8.")
print()
print()
print("You have reached the end!")
print("Your score is",str(score)+"/5")
time.sleep(15)