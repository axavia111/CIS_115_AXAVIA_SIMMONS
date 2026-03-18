#This program counts the frequency of each word in a given sentence




def word_frequency(my_sentence):
    words = my_sentence.split()
    frequency = {}

    for word in words:
        word = word.lower()

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


my_sentence = input("Enter a sentence: ") #Allow user to enter a sentence
print(word_frequency(my_sentence))