import argparse


class Laternfish(object):
    def __init__(self, timer):
        self.timer = timer

def parse_data(input_file):
    with open(input_file, 'r') as f:
        fish_timers = [int(fish_timer) for fish_timer in f.read().strip().split(',')]

    laternfish = [0] * 7
    for timer in fish_timers:
        laternfish[timer] += 1
    
    return laternfish

def calc_population(laternfish, days):
    fish_additions = [0] * 7
    for day in range(days):
        # Counting amount of fish given birth to
        day_idx = day % 7
        new_fish = laternfish[day_idx]

        # Adding the babies produced previously into the 
        # population
        laternfish[day_idx] += fish_additions[day_idx]
        fish_additions[day_idx] = 0

        # Adding babies to future population
        fish_additions[(day_idx + 2) % 7] = new_fish
    
    # realize that I need to add the ones that were not added yet
    return sum(laternfish) + sum(fish_additions)

if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 06')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()

    fish = parse_data(args.input_file)
    population = calc_population(fish, 80)
    print(population)
