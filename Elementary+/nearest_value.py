def nearest_value(values: set, one: int) -> int:
    # your code here
    values = sorted(values)
    diff = abs(one - values[0])
    num = values[0]

    for i in values:
        if i == one:
            return one
        else:
            new_diff = abs(one - i)
            if new_diff < diff:
                # if different between the next integer in "values"  and "one" is the new smallest difference,
                # take this as the new smallest "num"
                diff = new_diff
                num = i
    return num


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
