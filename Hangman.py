# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:58:58 2022

@author: USER
"""

from words import words
import random
import string

def get_word(words):
    random_word = random.choice(words)
    while '-' in words or ' ' in words:
        random_word = random.choice(words)
    
    return random_word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    
    while len(word_letters) > 0 and lives != 0:
        
        print (f"You have {lives} lives left.")
        print ("You have used these letters: ", " ".join(used_letters))

        letters_list = [] #[letter if letter in used_letters else '-' for letter in word]
        
        for letter in word:
            if letter in used_letters:
                letters_list.append(letter)
            else:
                letters_list.append('-')
        
        
        print ("You have Guessed: ", " ".join(letters_list))
        
        user_letter = input("Guess a Word: ").upper()
        
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in word_letters:
            print ("You have already used that character. Try Again!")
        else:
            print("Invalid Guess")
    
    print ("You have used these letters: ", " ".join(used_letters))
    
    letters_list = [letter if letter in used_letters else '-' for letter in word]
    
    print ("You have Guessed: ", " ".join(letters_list))
    
    if lives > 0:
        print ("Yay, You have guessed word correctly!")
    else:
        print ("Oops!, you lose!")
        print (f"The word was {word}!")
        

def main():
    hangman()

if __name__ == "__main__":
    main()