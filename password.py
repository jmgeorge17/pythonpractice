#Create a random password generator that has 5 numbers, 5 letters and 1 non-alpha character

import random
import string
import string_utils

def password():

    #Create new string
    new = ""

    #Start loop to collect a number of random numbers and letters
    for i in range(5):
        new += str(random.randint(0,9))
        new += random.choice(string.ascii_letters)

    #Collect a number of random punctuation characters
    new += random.choice(string.punctuation)

    #Print the shuffled string, providing a random order of characters
    print(string_utils.shuffle(new))

if __name__ == "__main__":
    password()