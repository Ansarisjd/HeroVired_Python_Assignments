import re


def check_password_strength(password):
    password_criteria = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    if re.match(password_criteria, password):
        return True 
    else:
        return False
    

Check_Password = input("Please enter your password")
result = check_password_strength(Check_Password)
print("Return:" , result)
