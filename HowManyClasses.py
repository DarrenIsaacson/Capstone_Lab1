classes = input("How many classes are you taking this year?")

class_List = [];

for itec_class in range(int(classes)):
    counter = itec_class + 1
    x = input("Enter in " + str(counter) + " class")
    class_List.append(x)

print("The classes that you are taking this year are:")

for each_course in class_List:
    print(each_course)
