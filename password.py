import random
import string

def generate_password(min_length,numbers=True,special_character=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    characters=letters
    if numbers:
        characters+=digits
    if special_character:
        characters+=special
        
    pwd=""
    criteria=False
    has_number=False
    has_special=False
    
    while not criteria or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char
        
        if new_char in special:
            has_special=True
        if new_char in digits:
            has_number=True
            
        criteria=True 
        if numbers:
            criteria=has_number
        if special_character:
            criteria = criteria and has_special
    return pwd
pwd=generate_password(10)  

print(pwd)