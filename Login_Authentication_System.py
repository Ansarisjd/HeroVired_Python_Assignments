def validate_login(username, password) :
    if len(username) <5 :
       print("Username must be atleast 5 chanracters long.")
       return False

    if len(password) <8: 
       print("Password must be atleast 8 characters Long.")
       return False
    
    has_digit = False
    for char in password:
       if char.isdigit():
         has_digit = True
         break

    if not has_digit:
       print("Error: Password must contain atleast one digit.")
       return False 
        
    print("Login Successful")
    return True 
 
username = input("Enter your username:")
password = input("Enter your password:")
result = validate_login(username, password)
print("Return:" , result)

