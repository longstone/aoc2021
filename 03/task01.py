import numpy as np

filename = "input/day03.txt"

def solver():
    with open(filename) as file:
        diagnostic_entry_length = (len(peek_line(file)) - 1)
        gamma_addition = empty_diagnostic_entry(diagnostic_entry_length)
        diagnostics = []
        for line in file:
            entry = map(lambda x: int(x), filter(lambda x: x == "1" or x == "0", split(line)))
            diagnostics.append(entry)
        for entry in diagnostics:
            array_with_single_binary_values = map(lambda x: int(x), split(entry))
            gamma_addition = array_plus_array(gamma_addition, array_with_single_binary_values)
        gamma = "".join(map(lambda x: str(x), map(lambda x: to_one_or_zero(x), gamma_addition)))
    epsilon = flip_bits(gamma)
    print "g {},\ne {}".format(gamma, epsilon)
    print "g {},\ne {}".format(int(gamma, 2), int(epsilon, 2))
    print "Solution => {}".format(int(gamma, 2) * int(epsilon, 2))


def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line


def split(word):
    return list(word)


def empty_diagnostic_entry(length):
    return [0] * length


def array_plus_array(base, additor):
    size = len(additor)
    result = np.copy(base)
    for i in range(size):
        value = zero_to_minus_one(additor[i])
        result[i] = int(base[i]) + value
    return result


def zero_to_minus_one(value):
    if value == 0:
        return -1
    return value


def to_one_or_zero(value):
    if value > 0:
        return 1
    elif value < 0:
        return 0
    elif value == 0:
        raise ValueError("value == zero - how to handle?")
    else:
        raise ValueError("sign on non number!")


def flip_bits(binary):
    # dirty
    return binary.replace('1', 'i').replace('0', '1').replace('i', '0')


solver()
