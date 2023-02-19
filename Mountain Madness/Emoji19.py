import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random
import time

nltk.download('wordnet')
def load_json(filename):
    import json
    # Open the file and load its contents into a variable
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data

def find_emoji(value):
    data = load_json('emojilib.json')
    for key in data:
        if value in data[key]:
            return key
    return None

#encrypts a given string into a string of emojis, 
# If no suitable emoji exists, the word is not replaced.
#returns the encrypted string and the amount of words replaced.
def encrypt_phrase(phrase):
    present_tense_sentence = present_tense(phrase)
    words = phrase.split()
    present_words = present_tense_sentence.split()
    emoji_string = ''
    count = 0
    for i,word in enumerate(present_words):
        emoji = find_emoji(word)
        if emoji == None:
            emoji = words[i]

        else:
            count += 1
       
        if emoji == words[i]:
             emoji_string += emoji + ' '
        
        elif(i>0 and emoji_string[i-1] != words):
             emoji_string += '  ' + emoji+'   '

        else:
             emoji_string += emoji + '  '


    return emoji_string, count


# Define a function to convert a sentence to present tense
def present_tense(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    # Replace each non-auxiliary verb in the sentence with its present tense form
    present_words = []
    for word, tag in nltk.pos_tag(words):
        if tag.startswith("VB") and word not in ["is", "am", "are", "was", "were", "be", "being",
                                                 "been", "have", "has", "had", "do", "does", "did", 
                                                 "will", "shall", "should", "would", "can", "could", 
                                                 "may", "might", "must"]:

            present_word = lemmatizer.lemmatize(word, 'v')
        
        else:
            present_word = word
        present_words.append(present_word)

    # Join the words back together into a sentence
    present_sentence = " ".join(present_words)
    return present_sentence

def choose_random_line(afile):
    lines = open(afile).read().splitlines()
    return random.choice(lines)

def select_file(filename):
    lines = open(filename).read().splitlines()
    random.shuffle(lines)
    return lines

if __name__ == "__main__":
    score = 0
    total = 0
    print("\nTHIS IS AN EMERGENCY! YOUR COMPUTER HAS BEEN HACKED BY THE EMOJI-19 VIRUS."+ 
            "IT HAS REPLACED RANDOM WORDS FROM YOUR PC WITH EMOJIS\n")
            
    name = input("enter your name... ")

    print("\nListen carefully {}! in order to proceed you must 🤔 all the emojis ✅-ly.\n".format(name)+
        "You'll be given 10 seconds for each guess. your test begins now.\n")

    while True:
        firstcheck = input("Choose an option to begin. \n"+
                        "1. Emoji-fy a personalized string? \n"+
                        "2. Guess the Emojized phrase, ☠️   CAUTION ☠️: Context will be lost in translation: \n")
        
        if(firstcheck == '2'):
            check2 = input("Select option for Data bank types\n"+
                        "1. Randomized (Difficulty: Easy)\n"+ 
                        "2. Poem Statements (Difficulty: Hard)\n"+ 
                        "3. Leave it to us: \n")

            file_name= ""

            if check2 == 1: file_name = "comprehensive.txt"
            elif check2 == 2: file_name = "poems.txt"
            else: file_name = "statements.txt"

            lines = select_file(file_name)

            for line in lines:
                try:
                    answer = encrypt_phrase(line)
                except:
                    continue
                if answer[1] < 2: continue

                print(answer[0])
                for x in range(10, 0, -1): 
                    print(x, end="... ", flush=True)
                    time.sleep(1)
                print("\n")
                
                print("The correct answer is: {}".format(line))
                check = input("Did you guess it right Y or N? \n"+
                            "THE EMOJI-19 VIRUS CAN TELL IF YOU'RE LYING "+
                            "(100% not a bluff, please trust me I just wanna go home): \n")

                if (check == 'Y' or check == 'y'):
                    score += 1
                
                total += 1

                quit = input("\nWould you like to quit? Y or N: ")
                if quit == 'y' or quit == 'Y':
                    break
            print("Your score for the game {} / {} ".format(score,total))

        else:
            string1 = input("Enter the string you wish to emoji-fy: ")
            answer = encrypt_phrase(string1)
            print("Your original string: " , string1, "\nhas been emojified to: ", answer[0])
        
        brk = input("would you like to go back to the options page? Y or N: \n")
        if brk == 'N' or brk == 'n': break
    
