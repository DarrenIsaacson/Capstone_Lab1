# This is a input statement for your name
name = input("What is your name?")
print("Hello ", name)
print()

# This is a input statement for your month and it checks to see if your input
# is similiar to the current month
birthday_month = input("What month were you born in?")
if(birthday_month == "January"):
    print("Happy Birthday Month")
else:
    print("You have entered:", birthday_month )

print()

# Iterates each character in the name variable.
for n in name:
    print(n)
print()
