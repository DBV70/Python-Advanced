text = input()

#unique_symbols = set()
#for ch in text:
#    unique_symbols.add(ch)

#unique_symbols = sorted(set(text))
#for ch in unique_symbols:
#    print(f"{ch}: {text.count(ch)} time/s")

[print(f"{ch}: {text.count(ch)} time/s") for ch in sorted(set(text))]