from qiskit_acqua import run_algorithm

rules = """
p cnf 3 2
-1 2 0
3 -2 0
"""


# allow rules to be provided or use default
def runGrover(r=rules):
    params = {
        'problem': {'name': 'search'},
        'algorithm': {'name': 'Grover'},
        'oracle': {'name': 'SAT', 'cnf': r},
        'backend': {'name': 'local_qasm_simulator'}
    }

    print("Starting Grover search")
    result = run_algorithm(params)
    print(result['result'])
    return result['result']


# convert a csv file to cnf
def csvTocnf(filename, query=[1,2]) :

    mapping = {}

    with open (filename, 'r') as file:

        # Only use the line of titles to
        # work out the number of variables the CNF will have
        x = file.readline()
        y = x.split(",")

        # Number of features is the same as the number of variables
        numFeatures = len(y) - 1

        # Number of lines is the same as the number of clauses
        numLines = 0

        overallCNF = ""
        for line in file.readlines():

            # Count the clauses
            numLines += 1

            parts = line.split(",")

            features = parts[1:]

            # lists can't be used as indices so convert to string
            featuresStr = "".join(features)

            # mapping between the config and a list of places which match
            if featuresStr not in mapping:
               mapping[featuresStr] = [parts[0]]
            else :
                mapping[featuresStr].append(parts[0])

            line = ""

            # iterate through the features and add them to the cnf
            for i in range (0, len(features)):
                toAdd = str(i +1)

                # if its 0, it needs to be negated
                if features[i].strip() == "0" :
                    toAdd = "-" + toAdd

                # Add the value to the line
                line = line + toAdd + " "

            # Append the 0 to show the line has ended
            line = line + "0"

            # Add this line to the overall buildup
            overallCNF = overallCNF + line + "\n"


        # Use the given query to allow the user to specify what they want
        queryLine = " ".join(str(n) for n in query) + " 0"

        # Add the necessary header for a DIMACS file
        titleLine  = "p cnf " + str(numFeatures) + " " + str(numLines + 1) + "\n"

        # Add all the parts together
        overallCNF = titleLine + overallCNF + queryLine

        # Return both the mapping and the cnf
        return (overallCNF, mapping)




def resultFromMapping(result, mapping):
    res = "".join(["1" if r > 0  else "0" for r in result])
    print(res)
    return mapping[res]


if __name__ == '__main__':
    (cnf, mapp) = csvTocnf("testLocation.csv")
    result = runGrover(cnf)
    resultFromMapping(result, mapp)

