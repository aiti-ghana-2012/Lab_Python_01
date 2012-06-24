"""
Lab_Python_01
Solution for Exercise 4
"""

#get input using raw_input(...)
first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")

print "Enter your date of birth:"

#indent using the escape character for tab '\t'
month = raw_input("\tMonth? ")
day = raw_input("\tDay? ")
year = raw_input("\tYear? ")

#print multiple items three ways

# 1. using string concatenation
print first_name + ' ' + last_name + ' was born on ' + month + ' ' + day + ', ' + year

# 2. using commas to print multiple items
print first_name, last_name, 'was born on', month, day+',', year

# 3. using string formatting (learn more by googling 'python string formatting'
print "%s %s was born on %s %s, %s" % (first_name, last_name, month, day, year)
