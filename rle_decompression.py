sequence = list(input("Insert sequence of bit (type: n*bit): ").split())
counter = []
result = []
support = []
count = 0
for i in range(len(sequence)):
    for j in range(len(sequence)):
        if sequence[i][j] != '*':
            count += 1
        else:
            break
    support.append(count)  # is the position of *, if we increase it by 1 we have the position of the number.
    counter.append(int(sequence[i][0:count]))  # in this way I extract what is before the * therefore the number of times the number appears.
    count = 0

for i in range(len(counter)):
    for j in range(counter[i]):
        result.append(sequence[i][support[i] + 1])  # thanks to a support list we can find the number also if there is multi-digit numbers.

for i in range(len(result)):
    print(result[i], end='')
