# This is a program that changes the sentences into a special formatting.

#  function that with maintain the program progression through the project
def main():

    # This is a function that will collect the users sentence that will be modified
    sentence = getsentence()

    # This is the function that will modify the sentence
    modify_sentence(sentence)

# The function that collets the sentence
def getsentence():

    # Throwing the inputted sentence into a variable
    sentence = input("What is the sentence that you are going to be modifying? :").lower()

    # Returning a split variable. Split property converts each space within the
    # sentence into a list where each word in a element.
    return sentence.split()

# This is the function that will modify the sentence
def modify_sentence(sentence):

    # For each statment that will iterate through each word
    for word in sentence:

        # We want to modify every element besides the first element in the list.
        # so here we are saying in this if-else Condition, for each word in the
        # list that is NOT the first element do something.
        if word != sentence[0]:

            # here we are modifying the first letter in each word
            print(word.title(), end='')
        else:
            # here we are converting the word into a lowercase word
            print(word.lower(), end='')



if __name__ == '__main__':
    main()
