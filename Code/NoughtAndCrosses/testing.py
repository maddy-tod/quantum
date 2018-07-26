import main
from randomPlayer import RandomPlayer
from TGatePlayer import TGatePlayer
from SGatePlayer import SGatePlayer
from contextlib import contextmanager
from GroverPlayer import GroverPlayer
import sys, os
from qiskit import  available_backends

oneVal = 'X'
twoVal = 'S'

# code from https://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def runTest(numTests, playerOne, playerTwo):

    countOne = 0;
    countTwo = 0;

    for i in range (0, numTests):
        result = main.playGameWithPlayers(playerOne, playerTwo)
        print(result)

        if result == oneVal:
            countOne += 1
        if result == twoVal:
            countTwo += 1


    return countOne, countTwo

def printStats(oneName, twoName, result):
    # from testing random against random
    exp1 = 0.58
    exp2 = 0.29
    expd = 0.13

    print("-----------")
    print(oneName + " was %.2f%% off just choosing randomly" % (((result[0] / numTests) - exp1) * 100))
    print(twoName + " was %.2f%% off just choosing randomly" % (((result[1] / numTests) - exp2) * 100))
    print(
        "Draw was %.2f%% off just choosing randomly" % ((((numTests - result[0] - result[1]) / numTests) - expd) * 100))


def createTest(playerOne, playerTwo, numTests=100):

    oneName =  playerOne.__class__.__name__
    twoName =  playerTwo.__class__.__name__

    print("Running " + str(numTests) + " tests of " + oneName+ " against "+ twoName)


    with suppress_stdout():
        result = runTest(numTests, playerOne, playerTwo)

    print(str(numTests) + " tests complete!")
    print(oneName+ " won " + str(result[0]) + " times")
    print(twoName + " won " + str(result[1]) + " times")
    print("A draw occurred " + str(numTests - result[0] - result[1]) + " times")

    printStats(oneName, twoName, result)

    print("-------------------------")

#createTest(GroverPlayer(oneVal) , RandomPlayer(twoVal), 20)
createTest(RandomPlayer(oneVal),  GroverPlayer(twoVal), 2)
#createTest(RandomPlayer(oneVal), RandomPlayer(twoVal))