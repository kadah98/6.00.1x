#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:39:52 2020

@author: kadah98
"""
import string

def isWordGuessed(secretWord, lettersGuessed):
    if len(secretWord) == 1:
        if secretWord in lettersGuessed:
            return True
        else:
            return False
    else:
        return (secretWord[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed)

def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = []
    for i in range(len(secretWord)):
        guessedWord.append('_ ')
        if secretWord[i] in lettersGuessed:
            guessedWord[i] = secretWord[i]
    return ''.join(guessedWord)

def getAvailableLetters(lettersGuessed):
    availableLetters = string.ascii_lowercase
    availableLetters = list(availableLetters)
    for char in lettersGuessed:
        if char in availableLetters:
            availableLetters.remove(char)
    return ''.join(availableLetters)

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long.")
    print("- - - - - - - - - - - -")
    mistakesMade = 1
    lettersGuessed = []
    while isWordGuessed(secretWord, lettersGuessed) == False and mistakesMade <= 8:
        print("You have", (9 - mistakesMade), "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        while letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print("- - - - - - - - - - - -")
            print("You have", (9 - mistakesMade), "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            letter = input("Please guess a letter: ")
        lettersGuessed.append(letter)
        if letter in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
        print("- - - - - - - - - - - -")
        
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord, ".")
    
hangman('car')
