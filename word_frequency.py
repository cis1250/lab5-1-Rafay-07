#!/usr/bin/env python3

# Word Frequency Exercise (Modular Version)
# TODO: (Read detailed instructions in the Readme file)
# The program now uses functions for modularity and reusability.
# 1. Prompt the user for a sentence.
# 2. Validate that it is a real sentence.
# 3. Split it into words and count how many times each appears.
# 4. Display the results.

import re

# making the function to check if the input is a valid sentence
def is_sentence(text):
    # Checking if the text isn't empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False
    # Checking for starting with a capital letter
    if not text[0].isupper():
        return False
    # Checking for ending punctuation (period, question mark, exclamation)
    if not re.search(r'[.!?]$', text):
        return False
    # Checking if it contains at least one word
    if not re.search(r'\w+', text):
        return False
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


# Function for calculating the frequency of each word
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
    print("Word frequencies:")  # heading for the output
    for i in range(len(words)):  # loop through both lists
        print(words[i] + ":", frequencies[i])  # print the word and its count

# Making a main function to organize the program flow
def main():
    sentence = get_valid_sentence()  # get a valid sentence from the user
    words, frequencies = calculate_word_frequency(sentence)  # calculate word counts
    display_frequencies(words, frequencies)  # display the results


# calling the main function to start the program
main()
