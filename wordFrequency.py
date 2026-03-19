#This program counts the frequency of each word in a given sentence




def word_frequency(my_sentence):
    words = my_sentence.split() #breaks the sentence into a list of words
    frequency = {} #starts an empty dictionary to track word counts

    for word in words: 
        word = word.lower() #makes sure the words in the sentence are all lowercased

        if word in frequency:
            frequency[word] += 1 #adds 1 to the existing count if the word is already found
        else:
            frequency[word] = 1 #sets the count to 1 the first time a new word is seen
    return frequency


my_sentence = input("Enter a sentence: ") #Allow user to enter a sentence
print(word_frequency(my_sentence)) #displays the final word count dictionary on the screen 