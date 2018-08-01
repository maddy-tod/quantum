import os

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

