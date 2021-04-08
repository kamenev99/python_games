
import random

guessesTaken = 0

print("Привет.Как тебя зовут?")
myName = input()

number = random.randint(1,20)
print("ну что ж, " + myName  + ", я загадываю число от 1 до 20.")

for guessesTaken in range(6):
    print("попробуй угадать.")
    guess = input()
    guess = int(guess)

    if guess > number:
        print("твое число слишком большое")

    if guess < number:
        print("твое число слишком маленькое")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("отлично " + myName + "! ты справился за " + guessesTaken + " попытки ")

if guess != number:
    number = str(number)
    print("Увы.Я загадала число " + number + ".")

