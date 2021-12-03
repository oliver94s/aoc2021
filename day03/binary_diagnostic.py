import argparse

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



if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 03')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()

    data = parse_data(args.input_file)
    result = diagnose(data)

    print(result)