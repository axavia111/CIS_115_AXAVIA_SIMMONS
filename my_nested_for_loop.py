#This program uses a nested for-loop to loop over list and print values

def printWordList():
    word = ['Apples','Bananas','Pears','Carrots']

    for item in word:
        print(item)
        for letter in item:
            print(letter)


printWordList()
    