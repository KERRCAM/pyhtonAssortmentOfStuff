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


def intInput(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            return userInput
            break
        except Exception:
            print("incorrect input")
            continue


def calculator():
    def add(current):
        numberToAdd = intInput("enter number to add to current: ")
        print("...")
        time.sleep(1)
        return current + numberToAdd

    current = int(intInput("enter starting number: "))
    calculating = True
    while calculating == True:
        function = intInput("what would you like to do to current number? (enter number of choice) (1)-add number- : ")
        if function == 1:
            current = add(current)
            print("new number is:")
            print(current)

def menu():
    choice = intInput("what would you like to use? (enter number of choice) (1)-calculator- : ")
    print("...")
    time.sleep(1)
    if choice == 1:
        calculator()


menu()
