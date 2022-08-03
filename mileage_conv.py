# This script takes distance in kilometers and converts to miles
# using user input for the initial length

#Get the user input
kms = input("Please enter the distance in kilometers: ")

# print("Ok, you said " + kms + ' kilometers')
miles = (float(kms) / 1.60934)

# raw float output
print("You traveled " + str(miles) + " miles")
# older method of .format to show 2 decimals
print("You traveled " + str('{0:.2f}'.format(miles)) + " miles")

# use round and f strings = new way
miles = round(miles, 2)
print(f"You traveled {miles} miles")

# a more complete statement
print(f"Your {kms} km ride is {miles} miles.")
