with open("currency.txt") as file:
    lines = file.readlines()

currencyDict = {}
for line in lines:
    split = line.split(" - ")
    currencyDict[split[0]] = split[1]

## primary
userCurrency = input("Your currency value- ")

## goal
print("\n\n\n\nEnter the currency you are convrting to - ")
print([key for key in currencyDict.keys()])
convertCurrency = input("Enter - ")

print(f"Your {userCurrency} in {convertCurrency} is {int(userCurrency) * float(currencyDict[convertCurrency])} ")