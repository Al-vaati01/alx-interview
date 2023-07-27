def pascal_triangle(n):
    final = []
    placeholder = 0
    count = 0
    if (n <= 0):
        return final

    while count < n:
        placeholder = (11 ** count)
        count += 1
        final.append([int(a) for a in str(placeholder)])
    for i in final:
        print(i, sep="\n")
