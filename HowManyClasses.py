# simple class program
classes = input("How many classes are you taking this year?")

# class list
class_List = [];

# This a for loop that will iterate based off the number of classes a student is taking
for itec_class in range(int(classes)):
    # Counter for formating
    counter = itec_class + 1

    # the users input
    x = input("Enter in " + str(counter) + " class")

    # adds to the list
    class_List.append(x)

print("The classes that you are taking this year are:")

# for each loop that iterates through each element of the for loop
for each_course in class_List:
    print(each_course)
