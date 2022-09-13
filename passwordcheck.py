def alphanumeric(password):
    if len(password) > 0 :
        if "_" and " " not in password:
            if password.isalnum():
                return True
    return False

password = ""
print(alphanumeric(password))