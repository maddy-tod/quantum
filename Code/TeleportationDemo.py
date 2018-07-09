import re
import random

global sendDir
global aQubit
global bQubit


def initialInfo():
    # Print greeting info
    print("Hello! Welcome to the quantum teleportation simulator")
    print("You have a qubit which is entangled with your friend Bob's")
    print("You are able to measure your qubits to see whether they point North, South, East or West")
    print("The result of this entanglement is that Bob's qubit will always be opposite to yours")

    # Allow the user to input which direction they wish to send Bob
    sendDirInp = input(
        "You wish to send Bob a message in the form of a direction. Which direction is it? Enter N, S, E or  W ").upper()

    # Validate the input
    while (sendDirInp != 'N' and sendDirInp != 'S' and sendDirInp != 'E' and sendDirInp != 'W'):
        print("Oops something was wrong with that input.")
        sendDirInp = input(
            "You wish to send Bob a message in the form of a direction. Which direction is it? Enter N, S, E or  W ")

    # Convert the compass direction to a number and store it
    global sendDir
    sendDir = dirToNum(sendDirInp)

    print("Great! You will send Bob the direction " + sendDirInp)


def entangle():
    global aQubit
    global sendDir
    print("What we must do now is entangle this direction with your half of the entangled pair and then measure it")
    print("Your qubit is currently in the state " + numToDir(aQubit) + " and the state you want to send is " + numToDir(
        sendDir))

    if sendDir % 2 == 0:
        aQubit = flip(aQubit)


    print("****************** entangling your direction with the member of the entangled pair you have ******************")
    print("After the entangling process your qubit is in the state " + numToDir(
        aQubit))
    print("We can see that the state to be transmitted is now " + numToDir(
        next(sendDir)) + " so it has been corrupted - so we have lost our copy :(")
    print("As we know Bob's qubit is always opposite to ours it must be in the state " + numToDir(flip(aQubit)))


def classicalTransmission():
    global sendDir
    global bQubit
    print("We now need to tell Bob how to change his qubit to make it match the state we wanted to send - " + numToDir(
        sendDir))
    print(
        "This part of the transportation must be done along classic means of communication which is why we can't have "
        "faster than light communication ")

    bQubit = flip(aQubit)

    print("To tell Bob enter a sequence of flips that will convert Bob's state (" + numToDir(
        bQubit) + ") into the state we wanted to send")

    seq = input("Use F to indicate a flip and N to indicate a rotation by 1 place clockwise")

    while not re.match("^[FN]+$", seq.upper()):
        print("Try again that input was invalid")
        seq = input("Use F to indicate a flip and N to indicate a rotation by 1 place clockwise")

    print("Great! Bob has received your transmission and is now applying it to his qubit")

    for char in seq:
        if char == 'F':
            bQubit = flip(bQubit)
        if char == 'N':
            bQubit = next(bQubit)


def bobResponse():
    b = "Bob : "
    print(b + "Hello!")
    print(b + "I have managed to recover a state")
    print(b + "It was " + numToDir(bQubit) + "!")
    correct = input(b + "Is that what you were trying to send me?! (Y/N)").upper()

    if correct == 'Y':
        print(b + "Yes! Quantum teleportation is really something")
    else:
        print(b + "Oh dear that really is a shame :( maybe the instructions were wrong ...")

    print("You have completed a quantum transportation simulation!")
    again = input("Would you like to go again? (Y/N)").upper()

    if again == 'Y':
        main()
    else:
        print("Bye-bye!")


def flip(x):
    return (x + 2) % 4


def next(x):
    return (x + 1) % 4


def dirToNum(x):
    return {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3
    }[x]


def numToDir(x):
    return {
        0: 'N',
        1: 'E',
        2: 'S',
        3: 'W'
    }[x]


def main():
    global aQubit
    aQubit = random.randint(0, 3)
    global bQubit
    bQubit = flip(aQubit)

    initialInfo()
    entangle()
    classicalTransmission()
    bobResponse()


main()
