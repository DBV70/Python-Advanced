class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

special_symbol = {"@", "*", "&", "%"}
password = input()
while password != "Done":

    digit = False
    letter = False
    special_sym = False
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    for ch in password:
        if ch.isdigit():
            digit = True
        elif ch.isalpha():
            letter = True
        elif ch in special_symbol:
            special_sym = True

    if (digit and not letter and not special_sym) or \
        (letter and not digit and not special_sym) or \
        (special_sym and not digit and not letter):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not special_sym:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    print("Password is valid")
    password = input()