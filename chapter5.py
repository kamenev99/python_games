import random
import time

def displayIntro():
    print("'ВЫ находитесь в землях, заселенных драконами.Перед собой вы видите две пещеры.В одной из них - дружелюбный дракон,который готов поделится с вами сокровищами.Во второй- жадный и голодный дракон,который вас сьест'")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
          print(" В какую пещеру вы войдете?(нажмите клавишу 1 или 2) ")
          cave = input()

    return cave

def checkCave(chosenCave):
    print("Вы приближаетесь к пещере...")
    time.sleep(2)
    print("Ее темнота заставляет вас дрожать от страха...")
    time.sleep(2)
    print("Большой дракон выпрыгивает перед вами!Он раскрывет свою пасть и ...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
          print("Делится с вами сокровищами")
    else:
         print(" ... Вас моментально сьедают ")
playAgain = "да"
while playAgain.strip() == "да" or playAgain == "д":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Попытаете удачу еще раз?( да или нет)")
    playAgain = input()
         
        

