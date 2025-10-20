#!/usr/bin/env python3
# Word Frequency Exercise (Modular Version)
# TODO: (Read detailed instructions in the Readme file)
# The program now uses functions for modularity and reusability.
# 1. Prompt the user for a sentence.
# 2. Validate that it is a real sentence.
# 3. Split it into words and count how many times each appears.
# 4. Display the results.

import re

# making a function that checks if the user's input is a proper sentence
def is_sentence(text):
    # checking if the text is actually a string and not empty
    if not isinstance(text, str) or not text.strip():
        return False  # return False if it's not valid text

    # checking if the first letter of the text is a capital letter
    if not text[0].isupper():
        return False  # return False if it doesn't start with a capital letter

    # checking if the sentence ends with a period, question mark, or exclamation mark
    if not re.search(r'[.!?]$', text):
        return False  # return False if it doesn’t end with proper punctuation

    # checking if the sentence has at least one word (not just spaces or symbols)
    if not re.search(r'\w+', text):
        return False  # return False if no words are found

    # if all checks pass, then it's a valid sentence
    return True

# Function for asking and validating the user's sentence
def get_valid_sentence():
    # keep asking until the user enters a valid sentence
    while True:
        user_sentence = input("Enter a sentence: ")  # asking the user for a sentence
        if is_sentence(user_sentence):  # check if the input meets the sentence criteria
            return user_sentence  # return the valid sentence
        else:
            print("This does not meet the criteria for a sentence.")  # tell the user it is invalid


# Function for calculating the frequency of each word using variable "sentence"
def calculate_word_frequency(sentence):
    # Convert sentence to lowercase so words are counted without case differences
    sentence = sentence.lower()

    # Remove punctuation marks from the sentence
    for char in ".!?,":  # removing these punctuation marks
        sentence = sentence.replace(char, "")

    # Split the sentence into a list of words
    words = sentence.split()

    # Create two empty lists: one for unique words, one for their frequencies
    unique_words = []
    frequencies = []

    # Go through each word in the list
    for word in words:
        if word in unique_words:  # check if the word is already in the list
            index = unique_words.index(word)  # find the position of the word
            frequencies[index] += 1  # increase the count at that position
        else:
            unique_words.append(word)  # add the new word to unique_words
            frequencies.append(1)  # start its count at 1

    return unique_words, frequencies  # returning both lists

# Making a function for displaying the results neatly
def display_frequencies(words, frequencies):
    # printing a heading to show what the following output means
    print("Word frequencies:")
    # using a for loop to go through each index in the list of words
    for i in range(len(words)):
        # printing each word followed by how many times it appeared
        print(words[i] + ":", frequencies[i])

# Making a main function to organize the program flow
def main():
    # calling the get_valid_sentence() function to ask the user for a proper sentence
    sentence = get_valid_sentence()
    
    # calling calculate_word_frequency() to count how many times each word appears
    words, frequencies = calculate_word_frequency(sentence)# this function gives back two lists: one with words and one with their counts
    
    # calling display_frequencies() to neatly print the results for the user
    display_frequencies(words, frequencies)

# calling the main function so the program actually runs
main()
