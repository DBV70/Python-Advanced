def age_assignment(*args, **kwargs):
    result = []
    for name in sorted(args):
        result.append(f"{name} is {kwargs[name[0]]} years old.")
    return "\n".join(result)

# test code
print(age_assignment("Peter", "George", G=26, P=19))
print("===============================")
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))