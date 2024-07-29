#pomodoro timer

import time
import os

def main():
    work_min = 0
    break_min = 0
    rounds = 0
    name = ""
    task = ""
    set_pomo(work_min, break_min, rounds, name, task)

def set_pomo(work_min, break_min, rounds, name, task):

    name = process_input("Hi there! What's your name? ", name, "", "We'd love to know your name!: ")
    task = process_input("What are your working on? ", task, "", "We'd love to know what you're working on!: ")
    work_min = process_input("Set work time (min): ", work_min, 0, "Invalid input. Please enter a positive value: ")
    break_min = process_input("Set break time (min): ", break_min, 0, "Invalid input. Please enter a positive value: ")
    rounds = process_input("Set number of rounds: ", rounds,  0, "Invalid input. Please enter a positive integer: ")

    pomo(name, task, work_min, break_min, rounds)

def process_input(prompt, var, val, errorPrompt):
    if val == "": # for name and task
        while var == val:
            var = input(prompt)
            if var == val:
                var = input(errorPrompt)
    elif prompt == "Set number of rounds: ":
        while var == val:
            try:
                var = int(input(prompt))
            except ValueError:
                var = val
                print(errorPrompt)
    else: #for timer
        while var == val:
            try:
                var = float(input(prompt))
            except ValueError:
                var = input(errorPrompt)
            if var == 0:
                var = input(errorPrompt)
    return var

def convert_to_seconds(time): #test this
    return int(time*60)

def intro(n, t, w, b, r): #test this
    return (f"{n} is working on {t} for {w*r} minutes with {b} minute breaks! Do not disturb!")


def countdown(t, label):
    while t:
        min, sec = divmod(t, 60) # t//60, t%60
        print(f"{label} {min:02d}:{sec:02d}", end = "\r")
        time.sleep(1)
        t -= 1

def pomo(name, task, work_min, break_min, rounds):
    work_sec = convert_to_seconds(work_min)
    break_sec = convert_to_seconds(break_min)
    for i in range(int(rounds)):
        os.system("clear||cls")
        print (intro(name, task, work_min, break_min, rounds), "\n")
        countdown(work_sec, "WORK")
        os.system("clear||cls")
        print (intro(name, task, work_min, break_min, rounds), "\n")
        countdown(break_sec, "BREAK")
    os.system("clear||cls")
    print("All done! Great job :)")

if __name__ == "__main__":
    main()