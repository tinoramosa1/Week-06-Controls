#TEST SCORE:

print("The test Scores program")
print()
print("Enter 999 to stop input")
print("========================")
print()

counter = 0
score_total = 0
test_score = 0

choice = "y"

while True:
    test_score = input("Enter test score: ")

    if test_score == "999":
        break
    elif (int(test_score) >= 0) and (int(test_score) <= 100):
        score_total += int(test_score)
        counter += 1
    else:
        print("Test score must be from 0 through 100. Try again>")

average_score = round(score_total / counter)

print("=======================")
print("Total Score: ", score_total)
print("Average Score: ", average_score)
print()

#GUESS THE NUMBER:

import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif num < guess:
        print("Wrong. Hint: lower")
    elif num > guess:
        print("Wrong. Hint: higher")
    else:
        print("ERROR")