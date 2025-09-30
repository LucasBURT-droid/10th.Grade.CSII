'''
Author: Lucas Burt 
Description: Methods to manipulate and interrogate an array of charaters
Bugs: Two letter names when attempt to get initals prints two of the last inital, Does not know if there is a middle name if there are multiple, does not work with numbers
Features: 15 unique functions to interrogate/manipulate an array of charaters 
Log: 1.1 - initial



'''








import random                                                                           # imports random letter




def display_name(name):   
    
    '''
    description - displays the user's input 
    args - the name (str): the users name
    returns- input/name of the user 
    
    
    '''
    
    print(f"Hello {name}! And Welcome!")                                                # uses an f string for placeholder in variable 
    
    display_name("lucas")

def vc(name):                                                                          # determines # of vowels + creates subtotals
   
    '''
    description - counts the vowels
    args - name (str): the user's name
    returns - vowel counter: int. number of vowels
    
    
    '''
    vowel_counter = 0
    vowels = ["a","i","e","o", "u","A","I","E","o","U"]

    for letter in name:                                                                 
        if letter in vowels:
            vowel_counter +=1
    return vowel_counter 


def cc (name):                                                                         # deternmines # of consonant + creates subtotals 
    
    '''
    description - counts consoants
    args - name (str): the user's name
    returns- consoant counter: int. number of consoants
    
    
    '''
    consonant_counter = 0 
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for letter in name: 
        if letter in consonants: 
            consonant_counter +=1 
    return consonant_counter

def get_last(name):                                                                     # Finds the last name from user
   
    '''
    description - finds the users last name
    args - name(str): the user's name
    returns- users last name 
    
    '''
    names = name.split(" ")                                                             # using the .split function to find the users last name
    #print(len(names))
    #print(names)
    if len(names) == 1:
        return names[0] 
    elif len(names) == 2: 
        return names [1]
    elif len(names) == 3: 
        return names [2]
    elif len(names) == 4: 
        return names [3]
    
        
    
def get_first(name):                                                                   # Finds the first name from user
   
    '''
    description - finds the users first name
    args - name (str): the user's name
    returns- user's first name
    
    
    '''
    fn = ""
    for letter in name:
        if letter == " ": 
            break 
        else: 
            fn = fn + letter 
    return fn
def get_middle(name):                                                                  # Finds the middle name from user 
   
    '''
    description - finds the users first name 
    args - name (str): the user's name
    returns- user's middle name
    
    '''
    names = name.split(" ")                                                            # uses the .split function to find the users middle name
    return names[1]


def check_hyphen(name):                                                                # checks for hyphen in name + creates subtotals 
    
    '''
    description - checks if there is a hyphen in user name
    args - name (str): the user's name 
    returns- hyphen counter: int. number of hyphens 
    
    '''
    hyphen = False                                                                         # hyphen counter
    for current_letter in name:                                                        # if statment 
        if current_letter == "-": 
            hyphen = True
            break
    
    return hyphen
    
def convrt_l(name):                                                                   # converts name to lowercase than dispalys to user
    
    '''
    description - converts user's name to lowecase 
    args - name (str): the user's name 
    returns- username in lowercase
    
    
    '''
    name_list = list(name) 
    new_list_name = [] 
    for c in name_list: 
        int_value = ord(c)                                                            #ascii convert
        if int_value < 90 and int_value >64: 
            int_value +=32
        lowercase_l = chr(int_value) 
        new_list_name.append(lowercase_l)
    return("".join(new_list_name))

def convrt_U(name):                                                                  # convert name to upperscase than displays to user
    
    '''
    description - converts user's name to uppercase 
    args - name (str): the user's name 
    returns- username in uppercase
    
    '''
    name_list = list(name)
    new_list_name =[]
    for c in name_list:
        int_value = ord(c)                                                           #ascii convert
        if int_value > 96 and int_value <128: 
            int_value -=32
        uppercase_L = chr(int_value) 
        new_list_name.append (uppercase_L)
    return("".join(new_list_name))

def scramblename(name):                                                             # Modify array to create a random name (scramble)
    
    '''
    description - scrambles the name of user
    args - name (str): the user's name 
    returns- the scrambled username
    
    
    '''
    name_list = list(name) 
    random.shuffle(name_list)                                                                # Randomly scrambles user name then prints
    return("".join(name_list))

def reverse_name(name):                                                              # Reverse and Display 
    
    '''
    description - takes string and reverses it 
    args - name (str): the user's name
    returns- the reversed name of user 

    '''
    return name[::-1]
    

def is_palidrome(name):                                                             # Checks if user name is/is not a palidrome 
    
    '''
    description - checks if users name is palindrome
    args - the name (str): user's name
    returns- message to user saying if name is/isnt a palidrome
    
    
    '''
    if name ==reverse_name:                                                         
        return True                                                                      # Output is a palidrome 
    else: 
        return False                                                                    # Output is not a palidrome

def intials(name):                                                                       # finds the users initals 

    '''
    description - gets user's initals 
    args - the name (str): user's name
    returns- message to user displaying their initals 
    
    
    '''
        
    print('name is: ' + name)
    fi = get_first(name)
    fi = fi[0]
    li = get_last(name) 
    li = li[0]
    mi = get_middle(name)
    mi = mi[0]

    output = fi + "." + mi + "." + li + "."

    return output 

def titles(name):                                                                   # finds title in user name (if applicable)
    '''
    description - gets user's title (if has one)
    args - the name (str): user's name
    returns- message to user displaying their title 
    
    
    '''
    Special_titles = ["Dr.","Mr.","Mrs.","Sir","Ms"]
    First_part_N = get_first(name) 
    if First_part_N in Special_titles: 
        return True 
    else: 
        return False 

def sortedarray(name):
    full_name = (input)
    array = list(name)
    array.sort()
    print(array)

'''
    description - sorts user's name into an array (Bonus Function)
    args - the name (str): user's name
    returns- message to user displaying their sorted name
    
    
    '''

    
def main():

    name = input("enter name ")
    print(f' Welcome {name}')
    while True:
        menu=input("""what do you want to do
        
        
        1 = Determine number of vowels in your name and display subtotal
        2 = Determine number of consants in your name and display subtotal    
        3 = Return last name 
        4 = Return first name
        5 = Return middle name 
        6 = Check if you have a hyphen in your name
        7 = Convert your name to lowercase 
        8 = Convert your name to uppercase
        9 = Scramble the letters in your name 
        10 = Find out if your name is or is not a palidrome  
        11 = Reverse and display your name            
        12 = Get your initals 
        13 = Find the title in your name than display 
        14 = Return full-name as a sorted array of characters 
        15 = Exit
        
        
        """)
        if menu == "11": 
            print(f"your name in reverse is: {reverse_name(name)}")
        elif menu == "1": 
            print(f"the number of vowels in your name is: {vc(name)}")
        elif menu == "2": 
            print(f"the number of consonants in your name is: {cc(name)}")
        elif menu == "3": 
            print(f"your last name is: {get_last(name)}")
        elif menu == "4": 
            print(f"your first name is: {get_first(name)}")
        elif menu == "5":
            print(f"your middle name is: {get_middle(name)}")
        elif menu == "6": 
            print(f" hyphens in your name: {check_hyphen(name)}")
        elif menu =="7": 
            print(f"Your name in all lowercase is: {convrt_l(name)}")
        elif menu =="8":
            print(f'Your name in all uppercase is: {convrt_U(name)}')
        elif menu == "9": 
            print(f'Your name scrambled is: {scramblename(name)}')
        elif menu == "10":
            print(f'pallindrome: {is_palidrome(name)}')
        elif menu == "11": 
            print(f'Your name reversed and displayed is: {reverse_name(name)}')
        elif menu == "12": 
            print(f"your intials are: {intials(name)} ")
        elif menu == "13": 
            print(f'your title is: {titles(name)}')
        elif menu == "14": 
            print(f'your name in a sorted array is: {sortedarray(name)}')
        elif menu == "15":
            break
        else: 
            print("ok")



    

main()

    

