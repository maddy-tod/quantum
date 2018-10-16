import os

import matplotlib.pyplot as plt

# Takes a dict of results and prints them with 3 column headings
def pprint(dict):
    print("Result      Count       Probability")
    print("-----------------------------------")

    # Store the formatted results strings
    results = []
    # Store the values from each result
    vals = []
    # Sum the values to get the overall number of tests
    total = 0;

    for key, val in dict.items():
        # Format the result to match the column headings and store it
        curr = str(key) + " " * (12 - len(key)) + str(val) + " " * (12 - len(str(val)))
        results.append(curr)

        # Store the value and increase the total
        vals.append(val)
        total += val

    # Iterate over the results and print
    i = 0
    for res in results:
        # Use the total to calculate probabilities
        print(res + "%.2f" % (vals[i] / total))
        i += 1


def getMax(dict) :

    maxVal = 0
    maxKey = ""
    for key, val in dict.items():
        if val > maxVal :
            maxVal = val
            maxKey = key

    return maxKey



# Takes the results dictionary and the name of a file
# Appends the dictionary to the file
def addToFile(dict, filename):
    try:
        # Check if the file is of the correct format
        with open(filename) as file:
            if file.readline() != "ADD\n":
                print("The file you have supplied does not support adding data.")
                return

        # Append the dictionary if the format is correct
        with open(filename, "a") as file:
            file.write("\n" + str(dict))

    # Create a new file and add the necessary header
    except FileNotFoundError:
        file = open(filename, "w+")
        file.write("ADD\n")

        # Write the data to be stored
        file.write(str(dict))
        file.close()


# Takes the results dictionary and the name of a file
# Updates the counts of the respective results in the file
def updateFileCounts(results, filename):
    try:
        # Check if the file is of the correct format
        with open(filename) as file:
            if file.readline() != "UPDATE\n":
                print("The file you have supplied does not support updating counts")
                return

            # Create a temporary file to allow the file to be copied over
            with open("temp.txt", "w+") as tfile:
                # Write the header
                tfile.write("UPDATE\n")

                # Iterate over the file, copying and incrementing counters as necessary
                for line in file.readlines():
                    parts = line.split(",")

                    # If this line is in the results, update the counts
                    # else just run the line
                    if parts[0] in results.keys():
                        tfile.write(parts[0] + "," + str(int(parts[1]) + results.get(parts[0])))
                        del results[parts[0]]
                    else:
                        tfile.write(line)
                # Copy over any new result
                for key, val in results.items():
                    tfile.write("\n" + str(key) + "," + str(val))
        # Rename the file to be the desired filename
        os.rename("temp.txt", filename)

    # Create a new file and add the necessary header
    except FileNotFoundError:
        file = open(filename, "w+")
        file.write("UPDATE\n")

        # Write all the data
        for key, val in results.items():
            file.write(str(key) + "," + str(val))

        file.close()


# Loads in the results from the given file
def loadFromFile(filename):
    raise Exception('Method not yet implemented')


# in future make axis depend on shots
def graph(dict, shots=1000):
    x = []
    y = []

    for k, v in dict.items():
        x.append(int(k, 2))
        y.append(v)

    plt.plot(x, y)
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.show()


def graphProbability(dict):
    # Sum the values to get the overall number of tests
    total = 0;

    x = []
    vals = []
    y = []

    for k, val in dict.items():
        x.append(int(k, 2))

        # Store the value and increase the total
        total += val
        vals.append(val)


    # Iterate over the results and print
    i = 0
    for v in vals :
        y.append(v/ total)

    plt.plot(x, y)
    plt.xlabel("Number")
    plt.ylabel("Probability")
    plt.show()


# Used to convert ; separated files into CSV files
def semiColonToCSV(filename) :
    try:
        # Check if the file is of the correct format
        with open(filename) as file:
            # Create a temporary file to allow the file to be copied over
            with open("temp.csv", "w+") as tfile:

                # Iterate over the file, copying and incrementing counters as necessary
                for line in file.readlines():
                    parts = line.split(";")
                    tfile.write(','.join(parts))


        # Rename the file to be the desired filename
        os.rename("temp.csv", filename)

    except FileNotFoundError:
        print("That file could not be found :(")


# NB must have category variable at the end
def transformCSV(filename):
    # take all the column titles
    # count rows
    try:
        # Check if the file is of the correct format
        with open(filename) as file:
            # read the titles
            topLine = file.readline()

            titles = topLine.split(",")
            # remove the last title as this is the category variable and so does not need a label
            titles = titles[:-1]


            lineCount = 0
            mapToNum = {}
            overallStr = ""
            # iterate over the other lines in the file
            for line in file.readlines():
                # add a new line
                lineCount +=1

                # split into each variable
                parts = line.split(",")
                currentStr = ""
                for i in range (0, len(parts)):
                    toAdd = 0

                    # use caps to standardize
                    currentVal = parts[i].upper()

                    # if numerical can already be used so just add it
                    if parts[i].isnumeric():
                       toAdd = currentVal
                    else :

                        # only will happen on 1st line
                        if mapToNum.get(i) is None :
                            mapToNum[i] = [currentVal]

                        # get the values associated with this index
                        listOfVals = mapToNum.get(i)

                        # if you haven't seen this value at this index before, add it

                        if currentVal not in listOfVals :
                            listOfVals.append(currentVal)

                        # the value corresponding to this string in this location
                        toAdd = listOfVals.index(currentVal.upper())

                    # Add this value to the overall sting
                    currentStr = currentStr + str(toAdd) + ", "

                # remove the final comma and space, and add a newline
                overallStr = overallStr + currentStr[:-2]  + '\n'

            # Finish up and write to file
            # Create 1st line
            topLine = str(lineCount) + "," + str(len(titles)) + "," + ",".join(titles)

            nameParts = filename.split(".")
            nameParts[0] += "-QMLREADY"

            with open('.'.join(nameParts), "w+") as outp :
                outp.write(topLine + '\n')
                outp.write(overallStr)


    except FileNotFoundError:
        print("That file could not be found :(")


def takeNumLines(filename, n):

    try:
        # Check if the file is of the correct format
        with open(filename) as file:
            # read the titles
            topLine = file.readline()


            # change the first number to be the new number of rows
            titles = topLine.split(",")
            titles[0] = str(n)

            # create a new filename to reflect the number of rows it contains
            nameParts = filename.split(".")
            nameParts[0] += str(n)


            # write out to this new file
            with open('.'.join(nameParts), "w+") as outp:

                # write the amended titles
                outp.write(','.join(titles))

                # write out all the other lines - not alterations needed
                while n > 0 :
                    outp.write(file.readline())
                    n-=1





    except FileNotFoundError:
        print("That file could not be found :(")

transformCSV("bankUSE.csv")

takeNumLines("bankUSE-QMLREADY.csv", 200)