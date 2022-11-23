def first_non_repeating_letter(string):
    if (len(string) <= 1): return string
    for i in string:
        check = 0
        for j in string:
            if i == j or i == j.lower() or i == j.upper():
                check += 1
                if check > 1: break
        if (check == 1) : return i
    return ''
print(first_non_repeating_letter('hello world, eh?'))