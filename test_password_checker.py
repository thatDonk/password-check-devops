from password_checker import is_valid_password

assert is_valid_password("password1") == False
assert is_valid_password("Password") == False
assert is_valid_password("PassW1") == False
assert is_valid_password("PASSWORD1") == False
assert is_valid_password("Password1") == True

