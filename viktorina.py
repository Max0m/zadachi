import time


print("Weolcome to  the science quiz!")
print("You have 5 questions to answer.")
score = 0


print("1. What is the smallest planet in the Solar System?")
one = input()
if one == "Mercury" or one == "mercury":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Mercury.")
print()
print()
print("2. Botany is the study of _______ ?")
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
print("3. How many wings does a bee have?")
three = input()
if three == "2" or three == "two" or three == "Two":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is two.")
print()
print()
print("4. What is the name of the largest ocean on earth?")
four = input()
if four == "Pacific" or four == "pacific":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Pacific.")
print()
print()
print("5. Calculate: 2+3*2")
five = input()
if five == "8" or five == "eight" or five == "Eight":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is 8.")
print()
print()
print("6. How many legs does a spider have?")
six = input()
if six == "8" or six == "eight" or six == "Eight":
    score = score + 1
    print("Correct!")
else: 
    print("Incorrect")
    print("The correct answer is 8.")
print()
print()
print("7. How many meters are there in a kilometer?")
seven = input()
if seven == "1000" or seven == "thousand" or seven == "Thousand":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is 1000.")
print()
print()
print("8. What is the biggest continent in the world?")
eight = input()
if eight == "asia" or eight == "Asia":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Asia.")
print()
print()
print("9. What is the biggest planet in our Solar System?")
nine = input()
if nine == "jupiter" or nine == "Jupiter":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Jupiter.")
print()
print()
print("10. What is the capital of America?")
ten = input()
if ten == "Washington D.C." or ten == "washington D.C." or ten == "washington" or ten "Washington":
    score = score + 1
    print("Correct!")
else:
    print("Incorrect.")
    print("The correct answer is Washington D.C.")
print()
print()
print("You have reached the end!")
print("Your score is",str(score)+"/10")
time.sleep(15)