def main():
    print_start_game() #print the start of the game
    path = input("Enter file path: ")
    num_of_words, secret_word =choose_word(path, int(input("Enter index: ")))
    #vars - 
    MAX_TRIES = 6
    num_of_tries = 0
    guessed = '' #the corrent guess
    old_letters_guessed = list()
    
    print("Let's start!")
    while not (check_win(secret_word, old_letters_guessed)) and num_of_tries <= MAX_TRIES:
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        #get unput and check it
        guessed = input("Guess a letter:")
        while not try_update_letter_guessed(guessed, old_letters_guessed):
            guessed = input("Guess a letter:")
        old_letters_guessed.append(guessed)
        #print after valid input:
        if guessed in secret_word:
            print(":(")
            print_hangman(num_of_tries)
        print(show_hidden_word(guessed, old_letters_guessed))
        num_of_tries += 1
    #end of game:
    print(show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")

def check_win(secret_word, old_letters_guessed):
    """checks if the user guessed the word
   :param secret_word: word to guess
   :param old_letters_guessed: the letter the users guessed
   :type secret_word: str
   :type old_letters_guessed: list
   :return: is the user guessed the word?
   :rtype: bool
   """
    secret_word_list = list(secret_word)
    counter = 0
    for char in secret_word_list:
        if char in old_letters_guessed:
            counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False

def show_hidden_word (secret_word, old_letters_guessed):
    """returns the letters the user guessed & '_' for these he didnt
   :param secret_word: the word the user need to guess
   :param old_letters_giessed: list of the letters the user guessed
   :type secret_word: str
   :type old_letters_giessed: list
   :return: srring of the letters the user guessed & '_' for these he didnt
   :rtype: str
   """
    guessed_letters = list() #list to return
    for char in secret_word:
        if char in old_letters_guessed:
            guessed_letters.append(char)
        else:
            guessed_letters.append("_")
    
    str_ = ' '.join(guessed_letters) #convert to srting & add spaces
    return str_

def check_valid_input (letter_guessed, old_letters_guessed):
    """checks if the user's input is valid (just letters & wasnt guessed)
   :param letter_guessed: the guess of the user
   :param old_letters_guessed: the old guesses of the user
   :type letter_guessed: char
   :type old_letters_guessed: list
   :return: is the input valid?
   :rtype: bool"""
    is_valid = False
    new_letter = False
    
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1):
        is_valid = True
    else:
        is_valid = False
    
    if letter_guessed.lower() in map(str.lower, old_letters_guessed):
        new_letter = False
    else:
        new_letter = True
    return is_valid and new_letter

def try_update_letter_guessed (letter_guessed, old_letters_guessed):
    """checks if the guess was valid & notify to user
   :param letter_guessed: the guessed letter
   :param old_letters_guessed: the old guesses of the user
   :type letter_guessed: char
   :type old_letters_guessed: list
   :return: is the input valid?
   :rtype: bool"""
    if check_valid_input (letter_guessed, old_letters_guessed):
        old_letters_guessed += [letter_guessed]
        return True
    else:
        print ("X")
        map(str.lower, old_letters_guessed)
        old_letters_guessed.sort(key=str)
        print (" -> ".join(old_letters_guessed[0::1]))
        return False
    
def choose_word (file_path, index):
    """get a path of file and an index - and return the words with the given index
    	:param file_path: the path of the file with the words
        :param index: the index of the word to return"""
    with open(file_path, 'r') as file:
        seen = list() #list of the words that already been
        read_file = file.read()
        list_of_words = list(' ') #first index with nothing (need to return index+1)
        list_of_words += (read_file.split(' ')) #the first index empty - the index starts at 1 and not 0
        counter_times = 0 #the number of time to run the loop
        word = ''
        i = 0 #index of the words in the list
        #find the words with the right index
        while counter_times != index:
            #find the word in the index
            if i == len(list_of_words)-1:
                i = 0
            word = list_of_words[i+1]
            i += 1
            counter_times += 1
            
        #counter of defferent words
        for i in range(len(list_of_words)):
            if list_of_words[i] not in seen:
                seen.append(list_of_words[i])
        
    return (len(seen)-1, word)
        
        
#print functions
def print_start_game ():
    print(print ("""
 _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
6
"""))
    
def print_hangman(num_of_tries):
    #create dict of photos - 
    HANGMAN_PHOTOS = {0: """
x-------x
""", 1: """
x-------x
    |
    |
    |
    |
    |
""", 2: """
    x-------x
    |       |
    |       0
    |
    |
    |
""", 3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}
    
    print(HANGMAN_PHOTOS[num_of_tries])
    
if __name__ == "__main__":
    main()