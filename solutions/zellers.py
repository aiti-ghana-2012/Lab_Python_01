"""
Lab_Python_01
Solution for Exercise 4
"""

#get input using raw_input(...)
first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")

print "Enter your date of birth:"

#indent using the escape character for tab '\t'
month = raw_input("\tMonth (1 - 12)? ")
day = raw_input("\tDay? ")
year = raw_input("\tYear? ")



#performing the adjustment that march is the first month
if int(month) < 3:
	zeller_month = int(month) + 10
	zeller_year = int(year) - 1
else:
	zeller_month = int(month) - 2
	zeller_year = int(year)


#now doing zellers algorithm
A = zeller_month
B = int(day)
C = zeller_year % 100 #to get the year of the century
D = zeller_year // 100 #to get the century

W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z % 7

if R < 0:
	R += 7

#using if / elif to turn R into a string
#think about how this could be done using a list!
if R == 0:
	day_of_week = 'Sunday'
elif R == 1:
	day_of_week = 'Monday'
elif R == 2:
	day_of_week = 'Tuesday'
elif R == 3:
	day_of_week = 'Wednesday'
elif R == 4:
	day_of_week = 'Thursday'
elif R == 5:
	day_of_week = 'Friday'
elif R == 6:
	day_of_week = 'Saturday'



#print multiple items three ways

# 1. using string concatenation
print first_name + ' ' + last_name + ' was born on ' + day_of_week + ', ' + month + ' ' + day + ', ' + year

# 2. using commas to print multiple items
print first_name, last_name, 'was born on', day_of_week+',', month, day+',', year

# 3. using string formatting (learn more by googling 'python string formatting'
print "%s %s was born on %s, %s %s, %s" % (first_name, last_name, day_of_week, month, day, year)
