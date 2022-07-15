# Mayolo Valencia
# 10/21/2021
# User inputs their word or sentence then it is
# translated to pig latin using the functions to
# change up the string.

def to_pig(word):
    """ looks if the word has a vowel in the first index
        and treats it differently than if it started with
        a consonants
        
        If it starts with a vowel add "way" at the end if
        it starts with a consonants, until it spots a vowel
        it will bring those consonants to the end and add "ay".
    """
    word = word.lower()
    vowels = "aeiouy"
    pig_word = ""
   
    if word[0] in vowels:
        pig_word = word + "way"
    else:
        count = 1
        while count < len(word) and word[count] not in vowels:
            count += 1
            
        pig_word = word[count:] + word[0:count] + "ay"
            
    return pig_word

def pig_sentence(word):
    """ Splits the string into separate words then translates
        each word using the to_pig method and puts it back
        together into a solid string.
    """
    word_list = word.split()
    pig_sentence = ""
    for word in word_list:
        pig_word = to_pig(word)
        pig_sentence += pig_word + " "
    return pig_sentence

def main():
    """ User inputs their string then the method decides
        if its a string or not and chooses its function.
    """
    normal_text = input("What do you want to translate to pig latin: ")

    
    print("Translated sentence is:", '"', pig_sentence(normal_text), '"')

# call main to run the function
main()