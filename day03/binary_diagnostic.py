import argparse
import copy


def parse_data(input_file):
    with open(input_file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    return data

def diagnose(data):
    data_len = len(data[0])
    
    gamma = [None] * data_len
    epsilon = [None] * data_len

    majority = len(data) / 2
    for col in range(data_len):
        one = 0
        zero = 0
        for row in range(len(data)):
            if data[row][col] == '0':
                zero += 1
            else:
                one += 1
            
            if zero > majority:
                gamma[col] = "0"
                epsilon[col] = "1"
                break
            elif one > majority:
                gamma[col] = "1"
                epsilon[col] = "0"
                break
    
    gamma_rate = int("".join(gamma), 2)
    epsilon_rate = int("".join(epsilon), 2)
    return gamma_rate * epsilon_rate


def filter_oxygen(data, col_num):
    print(len(data), col_num)
    if len(data) < 6:
        print("\n".join(data))
    majority = len(data) / 2
    
    # determine majority
    # using this list's index to determine the number
    count = [[], []]
    for d in data:
        count[int(d[col_num])].append(d)

    if len(count[0]) > majority:
        return count[0]
    elif len(count[1]) > majority:
        return count[1]
    
    if len(count[1]) != len(count[0]):
        print('something went wrong')
    
    return count[1]

def filter_c02(data, col_num):
    if len(data) == 1:
        return data
    majority = len(data) / 2
    
    # determine majority
    # using this list's index to determine the number
    count = [[], []]
    
    for d in data:
        count[int(d[col_num])].append(d)

    # return whatever has the least, if equal return count[0]
    if len(count[0]) > majority:
        return count[1]
    elif len(count[1]) > majority:
        return count[0]
    elif len(count[1]) == len(count[0]):
        return count[0]


def oxygen_diagnose(data):
    data_len = len(data[0])
    
    oxygen = copy.deepcopy(data)
    c02 = copy.deepcopy(data)
    
    for col in range(data_len):
        oxygen = filter_oxygen(oxygen, col)
        c02 = filter_c02(c02, col)

    print(oxygen)
    oxygen_rate = int("".join(oxygen), 2)
    print(c02)
    c02_rate = int("".join(c02), 2)

    return oxygen_rate * c02_rate


if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 03')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()

    data = parse_data(args.input_file)
    result = diagnose(data)
    print(result)

    print(oxygen_diagnose(data))