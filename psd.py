import random

def generate_password():
   
    user_input = input("Enter the characters you want to include in the password: ")

   
    if len(user_input) < 8:
        print("You must enter at least 8 different characters.")
        return
    
    
    password = ''.join(random.sample(user_input, 8))
    
  
    print("Generated Password:", password)

generate_password()
