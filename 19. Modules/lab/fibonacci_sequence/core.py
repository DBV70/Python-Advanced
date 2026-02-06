def create_sequence(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(n, seq):
    try:
        index = seq.index(n)
        return f"The number - {n} is at index {index}"
    except ValueError:
        return f"The number {n} is not in the sequence"