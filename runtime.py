def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(n)         ]


    """

    if len(s1) != len(s2):  # O(1)
        return False

    for i in range(len(s1)):  # O(n)
        if s1[i] != s2[i]:  # O(1)
            return False

    return True

    # 1 + (n * 1) = 1 + n = n
    # O(n)


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [      O(n)         ]

    """

    if "hippo" in animals or "platpypus" in animals:  # O(n) b/c need to iterate through list each time and see if word is in list
        return True
    else:
        return False

    # O(n)


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n^2)         ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers) # O(n)

    for x in s:  # O(n)
        if -x in s:  # O(n)
            result.append([-x, x])  # O(1)

    return result

    # n + (n * n + 1) = n + n^2 = 2n^2
    # O(n^2)


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n^2)         ]

    """

    result = []

    for x in numbers:  # O(n)
        for y in numbers:  # O(n)
            if x == -y:  # O(1)
                result.append((x, y))  # O(1)
    return result

    # n * n * 1 * 1 = n^2
    # O(n^2)


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [      O(n^n)         ]

    """

    result = []

    for x in numbers:  # O(n)
        for y in numbers:  # O(n)
            if x == -y and (y, x) not in result:  # O(n)
                result.append((x, y))  # O(1)
    return result

    # n * n * n * 1 = n^3
    # O(n^n)
