def pascal_triangle(n):
    final = []
    out = []
    placeholder = 0
    count = 0
    if (n <= 0):
        return final

    while count < n:
        placeholder = (11 ** count)
        count += 1
        out = [int(i) for i in str(placeholder)]
        convert = [int(i) for i in out]

        final.append(convert)
    print(final)


pascal_triangle(5)
