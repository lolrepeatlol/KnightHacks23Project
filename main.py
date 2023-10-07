import math
# opens file
statement = open("September2023_2442.csv", "r")
# print("Name of the file: ", statement.name)
# takes each line in a file and puts it in a list
listOfStatements = statement.readlines()
untilChar = '",'
allTransactionsString = []
allTransactionsFloat = []
counterForArray = 0
sumOfTransactionNotR = 0
sumOfTransactionR = 0
for x in listOfStatements:
    # gets rid of necessary white space
    x = x.strip()
    if untilChar in x:
        # if the until char is found in the line of the file we split it to the content after the car until char
        contentAfterStart = x.split(untilChar, -2)[-1]
        # inserting the split content into a string array
        allTransactionsString.insert(counterForArray, contentAfterStart)
        # counter for the array
        counterForArray += 1
        # print(allTransactionsString)
# changes the string to positive and changes it to float and stores it in a float array
for element in allTransactionsString:
    # subtracts the first char from the string
    newString = element[1:]
    # changes the string to a float so we can store it into an float array later to use
    newElement = float(newString)
    allTransactionsFloat.append(newElement)
print("old transaction", allTransactionsFloat)
counterForArray = 0
sumOfRoundedUp = 0
for transaction in allTransactionsFloat:
    oldTransaction = transaction
    sumOfTransactionNotR += allTransactionsFloat[counterForArray]
    allTransactionsFloat[counterForArray] = math.ceil(transaction)
    sumOfRoundedUp += abs(allTransactionsFloat[counterForArray] - oldTransaction)
    sumOfTransactionR += allTransactionsFloat[counterForArray]
    counterForArray += 1
sumOfRoundedUp = round(sumOfRoundedUp, 2)
print("New ", allTransactionsFloat, "\n")
print("sum of round ups", sumOfRoundedUp)
print("sum of transactions without added roundup:", sumOfTransactionNotR)
print("sum of transactions after roundup:", sumOfTransactionR)

statement.close()
