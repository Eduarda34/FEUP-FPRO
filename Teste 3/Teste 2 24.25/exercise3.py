def remove_consecutive_duplicates(astr):
    res = ""

    for i in range(len(astr) - 1):
        if astr[i] != astr[i+1]:
            res += astr[i]

    res += astr[-1]

    return res

print(remove_consecutive_duplicates("heeeellllooooooo"))
print(remove_consecutive_duplicates("ananas"))
print(remove_consecutive_duplicates("bookkeeper"))
print(remove_consecutive_duplicates("x"))