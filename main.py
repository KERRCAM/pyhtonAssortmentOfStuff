import random
import time
import math


def stringInput(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            return userInput
            break
        except Exception:
            print("incorrect input")
            continue


def calculator():
    print(2)


def menu():
    choice = stringInput("what would you like to use? (enter number of choice) (1)-calculator- : ")
    if choice == 1:
        calculator()


menu()
