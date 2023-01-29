sequence = input("Insert sequence of bit: ")
count = 1
result = []
for i in range(len(sequence)):
    try:
        if sequence[i] == sequence[i + 1]:
            count += 1
        else:
            result.append(f"{count}*{sequence[i]}")
            count = 1
    except Exception:
        result.append(f"{count}*{sequence[i]}")


print(result)
