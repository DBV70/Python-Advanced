valid_domains = {".com", ".bg", ".net", ".org"}
class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


while True:
    email = input()
    if email == "End":
        break
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name = email.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = "." + email.split(".")[-1].strip()
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")

# abc@abv.bg
# End

# peter@gmail.com
# petergmail.com
# End