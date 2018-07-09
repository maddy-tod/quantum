import main
from randomPlayer import RandomPlayer
from contextlib import contextmanager
import sys, os


oneVal = 'X'
twoVal = 'O'

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

def createTest(playerOne, playerTwo, numTests=100):

    print("Running " + str(numTests) + " of " + playerOne.__class__.__name__ + " against "+ playerTwo.__class__.__name__ )


    with suppress_stdout():
        result = runTest(numTests, playerOne, playerTwo)

    print(str(numTests) + " tests complete!")
    print(oneVal + " won " + str(result[0]) + " times")
    print(twoVal + " won " + str(result[1]) + " times")
    print("A draw occurred " + str(numTests - result[0] - result[1]) + " times")


createTest(RandomPlayer(oneVal), RandomPlayer(twoVal), 200)
