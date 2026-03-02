'''
Author: Lucas Burt 
Description: This program reads text files of plays, cleans the text by removing punctuation and converting it to lowercase, counts the frequency of each word, filters out common words (stopwords), and prints the top frequent words to the console. It also saves the top frequent words to a CSV file for further analysis.
Bugs: None Known 
Sources: Google, W3 Schools
Dates: 2/19/26 
Features: 
    - Reads text files of plays
    - Cleans text by removing punctuation and converting to lowercase
    - Counts word frequency
    - Filters out common words (stopwords)
    - Prints top frequent words to console
    - Saves top frequent words to CSV file
'''

import string

def read_file(file_name):
    '''
    description - Reads a text file, processes the text to count word frequencies, and saves the top frequent words to a CSV file.
    args - file_name (str): The name of the text file to read and analyze.
    returns- None
    '''
    try:
        fhand = open(file_name, "r")
        counts = dict()
    
        for line in fhand:
            line = line.rstrip()
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else: 
                    counts[word] += 1
        #Removes Stopwords
        words_to_delete = ["enter","more", "well", "let","man" "know","all","ill","a", "an", "the", "and", "or", "but", "nor", "so", "yet", "of", "to", "in", "for", "on", "at", "by", "from", "with", "about", "into", "through", "over", "after", "before", "between", "under", "without", "i", "me", "my", "mine", "you", "your", "yours", "he", "him", "his", "she", "her", "hers", "we", "us", "our", "ours", "they", "them", "their", "theirs", "thou", "thee", "thy", "thine", "is", "am", "are", "was", "were", "be", "been", "being", "do", "does", "did", "have", "has", "had", "shall", "will", "would", "should", "can", "could", "may", "might", "must", "that", "this", "these", "those", "which", "who", "whom", "whose", "what", "when", "where", "why", "how", "not", "no", "yes", "if", "then", "so", "as", "it", "its", "itself", "there", "here", "now", "than", "too", "very", "o","come","sir","regan"] 
        counts2 = counts.copy()
        for k in counts2.keys(): 
            if k in words_to_delete: 
                del counts[k] 
        #Sorts the dictionary by frequency and then alphabetically
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        sorted_freq_dict = dict(sorted_items)
        print(sorted_freq_dict)
        count = 0 
        limit = 15
        #Saves the top 15 most frequent words to a CSV file
        if file_name == "King_Lear.txt":
                    input2 = open("King_Lear.csv", "w")
        elif file_name == "Midsummer_Nights_Dream.txt":
                    input2 = open("Midsummer_Nights_Dream.csv", "w")
        #Prints the top 15 most frequent words to the console and saves them to the CSV file
        for key, value in sorted_freq_dict.items(): 
            if value > 15:
                 print(key + " " +str(value))
                 input2.write(key + "," + str(value) + "\n")
                 count = count + 1
                 if count == limit:
                      break
    except FileNotFoundError:
        print(f'File cannot be opened:, {file_name}')
        exit()

def main (): 
    """
    Main program function: Provides a menu to select which play to analyze.
    Options: 1. King Lear or 2. Midsummer Night's Dream
    """
    print("""
1 King_Lear 
2 Midsummer Night's Dream 
        """)
    option = input("what would you like to do?: 1. King Lear 2. Midsummer Night's Dream  ")       
    
    if option == '1':  
        read_file("King_Lear.txt") 
    elif option == '2':
        read_file("Midsummer_Nights_Dream.txt")


if __name__ == "__main__":
    main()

