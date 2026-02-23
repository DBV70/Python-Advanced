def negative_vs_positive(*args):
    n_sum = sum([num for num in args if num < 0])
    p_sum = sum([num for num in args if num > 0])
    return n_sum, p_sum

numbers = map(int, input().split())

neg_sum, pos_sum = negative_vs_positive(*numbers)
print(neg_sum)
print(pos_sum)
if abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
