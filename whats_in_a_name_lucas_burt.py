import random

def display_name(name):                                                                 #name = Paramiter 
    print(f"Hello {name}! And Welcome!")                                                #for F string, use curly brackets  for placeholder in variable 
    
    display_name("lucas")

def vc (name):                                                                          #determines # of vowels + creates subtotals
    vowel_counter = 0
    vowels = ["a","i","e","o", "u","A","I","E","o","U"]

    for letter in name:     
        if letter in vowels:
            vowel_counter +=1
        print(vowel_counter)
    return vowel_counter 


def cc (name):                                                                         # deternmines # of consonant + creates subtotals 
    consonant_counter = 0 
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for letter in name: 
        if letter in consonants: 
            consonant_counter +=1 
        print(consonant_counter)
    return consonant_counter

def get_last(name):                                                                     # Finds the last name from user
    names = name.split(" ")  
    if len(names) == 1:
        return name[0] 
    if len(names) == 2: 
        return name [1]
    if len(names) == 3: 
        return name [2] 
    
def get_first(name):                                                                   # Finds the first name from user
    fn = " "
    for letter in name:
        if letter == "": 
            break 
        else: 
            fn = fn + letter 
def get_middle(name):                                                                  # Finds the middle name from user 
    names = name.split(" ")
    return name [2]

def check_hyphen(name):                                                                # checks for hyphen in name + creates subtotals 
    hyphen = 0 
    for current_letter in name: 
        if current_letter == "-": 
            hyphen +=1 
            break
    
    return hyphen
    
def convrt_l(name):                                                                   # converts name to lowercase than dispalys to user

    name_list = list(name) 
    new_list_name = [] 
    for c in name_list: 
        int_value = ord(c) #ascii convert
        if int_value < 90 and int_value >64: 
            int_value +=32
        lowercase_l = chr(int_value) 
        new_list_name.append (lowercase_l)
    return("".join(new_list_name))

def convrt_U(name):                                                                  # convert name to upperscase than displays to user

    name_list = list(name)
    new_list_name =[]
    for c in name_list:
        int_value = ord(c)
        if int_value < 96 and int_value >128: 
            int_value -=32
        uppercase_L = chr(int_value) 
        new_list_name.append (uppercase_L)
    return("".join(new_list_name))

def scramblename(name):                                                             # Modify array to create a random name (scramble)
    list = (name) 
random.shuffle(list)
print(list)

def reverse_name(name):                                                              # Reverse and Display 
    return name [::-1]
    

def is_palidrome(name): 
    if name ==reverse_name: 
        print("your name is a palidrome") 
    else: 
        print ("your name is not a palidrome")






def main():

    name = input("enter name ")
    print(f' Welcome {name}')
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
        print(f"your middle name is: {get_first(name)}")
    elif menu == "6": 
        print(f"the amount of hyphen's you have: {check_hyphen(name)}")
    elif menu =="7": 
        print(f"Your name in all lowercase is: {check_hyphen(name)}")
    elif menu =="8":
        print(f'Your name in all uppercase is {convrt_U(name)}')
    


    

    vowels = vc(name) 



    hyphen_found = check_hyphen(name)
    if hyphen_found == 1:
        print("hyphen found") 
    
    hyphen_Notfound = check_hyphen(name)
    if hyphen_Notfound == 0: 
        print("hyphen not found ")

    print(vowels)


    

main()

    