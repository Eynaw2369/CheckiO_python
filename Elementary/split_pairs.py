def split_pairs(a):
    # your code here
    split_into_list = []
    for i in range(0, len(a), 2):
        split_list = a[i:i+2]
        split_into_list.append(split_list)

    output = []
    for i in split_into_list:
        if len(i) != 2:
            output.append(''.join(i + '_'))
        else:
            output.append(i)
    return output


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
