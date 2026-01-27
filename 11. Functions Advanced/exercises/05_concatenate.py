def concatenate(*args, **kwargs):
    text = ''.join(args)
    for key, value in kwargs.items():
        text = text.replace(key, value)
    return text

#test code
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))