import argparse


def parse_data(input_file):
    with open(input_file, 'r') as f:
        crab_subs = [int(crab_sub) for crab_sub in f.read().strip().split(',')]
    
    return crab_subs

def calc(crab_subs, pos):
    total = 0
    for sub in crab_subs:
        total += abs(sub - pos)
    
    return total

cached_sums = {}

def calc2(crab_subs, pos, best):
    total = 0
    for sub in crab_subs:
        delta = abs(sub - pos)
        subtotal = cached_sums.get(delta, 0)
        if not subtotal:
            for x in range(delta + 1):
                subtotal += x
            cached_sums[delta] = subtotal
        total += subtotal
        
        if best is not None and total > best:
            return total
    
    return total

def calc_most_efficient(crab_subs):
    most_efficient = None 
    best_pos = None
    for pos in range(min(crab_subs), max(crab_subs)):
        gas_usage = calc2(crab_subs, pos, most_efficient)
        if most_efficient is None or most_efficient > gas_usage:
            most_efficient = gas_usage
            best_pos = pos

    return most_efficient, best_pos

if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 07')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()

    crabs = parse_data(args.input_file)
    gas, pos = calc_most_efficient(crabs)
    print(gas, pos)
