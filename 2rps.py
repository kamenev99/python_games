import random

print("")
print("Stone| Paper | Scissors ")
print("")
playAgain = "да"
while playAgain == "да" or playAgain == "д":
    a = random.randint(1,3)


    if a == 1:
        b = "камень"

    elif a == 2:
        b = "ножницы"

    else:
        b = "бумага"

    print(" 1 камень, 2 ножницы , 3 бумага")

    с = int(input("Введите цифру : "))
    if с == 1:
        print("Ты выбрал камень")
        print(" Твой соперник выбрал ... " + str(b))
        if a == 1:
            print("Ничья")
        elif a == 2:
            print("Молодец!!!ТЫ ПОБЕДИЛ")
        else:
            print("Ты проиграл .......")
    elif с == 2:
        print("Ты выбрал ножницы")
        print(" Твой соперник выбрал ... " + str(b))
        if a == 1:
            print("Ты проиграл...")
        elif a == 2:
            print("Ничья")
        else:
            print("Молодец!!!ТЫ ПОБЕДИЛ!!!")
    elif с == 3:
        print("Ты выбрал бумагу")
        print(" Твой соперник выбрал ... " + str(b))
        if a == 1:
            print("ТЫ ПОБЕДИЛ.Молодец!!!")
        elif a == 2:
            print("Ты Проиграл...")
        else:
            print("Ничья")
    print("Попытаете удачу еще раз?( да или нет)")
    playAgain = input()
    playAgain = playAgain.strip()


