num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

more_prev = [num[i + 1] for i in range(len(num) - 1) if num[i + 1] > num[i]]
print(more_prev)
