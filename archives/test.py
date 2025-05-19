def normalise_instructors(raw):
    """
    Merge any instructor that ends with a comma with the instructor(s)
    that immediately follow it.

    >>> normalise_instructors(
    ...     ["Kaishu Wu,", "Andrew Bauer,", "Jerry Zhou,", "John Doe"]
    ... )
    [['Kaishu Wu', 'Andrew Bauer, Jerry Zhou'], 'John Doe']
    """

    i = 0
    n = len(raw)
    out = []
    while i < n:
        if raw[i].endswith(","):
            merged = [raw[i].rstrip(",")]

            while i + 1 < n and raw[i + 1].endswith(","):
                merged.append(raw[i + 1].rstrip(","))
                i += 1

            i += 1
            if i >= n:
                raise ValueError("List ends with a dangling comma.")

            merged.append(raw[i])
            out.append(merged)
        else:
            out.append(raw[i])

        i += 1

    return out


instructors = ["Kaishu Wu,", "Andrew Bauer", "Jerry Zhou,", "John Doe"]

print(normalise_instructors(instructors))
