import argparse


class VentMap(object):
    def __init__(self, max_x, max_y):
        self.map = self._init_map(max_x, max_y)

        self.vent_count = 0
    
    def _init_map(self, max_x, max_y):
        rtn_map = []
        for idx in range(max_y + 1):
            rtn_map.append([0] * (max_x + 1))
        return rtn_map
    
    def print_map(self):
        for row in self.map:
            row_str = [str(vent) for vent in row]
            print(''.join(row_str))
    
    def calc_line(self, src, dest):
        delta_x = dest[0] - src[0]
        delta_y = dest[1] - src[1]

        if abs(delta_y) and abs(delta_x) and not abs(delta_y) == abs(delta_x):
            return
        
        self.vent_count += 1

        x_step = 1 if delta_x > 0 else -1
        y_step = 1 if delta_y > 0 else -1
        
        start_x = src[0]
        start_y = src[1]
        
        if abs(delta_y) == abs(delta_x):
            for x in range(0, abs(delta_x + x_step), abs(x_step)):
                x_pos = start_x + (x_step * x)
                y_pos = start_y + (y_step * x)
                self.map[y_pos][x_pos] += 1
        elif abs(delta_x) > 0:
            for x in range(0, delta_x + x_step, x_step):
                # print("x: %s" % x)
                self.map[start_y][start_x + x] += 1
        elif abs(delta_y) > 0:
            for y in range(0, delta_y + y_step, y_step):
                # print("y: %s" % y)
                self.map[start_y + y][start_x] += 1
        
        # print("src: %s\tdest: %s" % (src, dest))
        # self.print_map()

        # print('')

    def calc_overlaps(self):
        count = 0
        for row in self.map:
            for col in row:
                if col > 1:
                    count += 1
        print("overlaps: %s" % count)        
        return count

def parse_data(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    vents = []
    max_x = 0
    max_y = 0
    for line in lines:
        left, right = line.split('->')

        src = [int(x) for x in left.strip().split(',')]                
        dest = [int(x) for x in right.strip().split(',')]

        if src[0] > max_x:
            max_x = src[0]
        if src[1] > max_y:
            max_y = src[1]

        if dest[0] > max_x:
            max_x = dest[0]
        if dest[1] > max_y:
            max_y = dest[1]

        vents.append( (src, dest) )
    print("max x: %s" % max_x)
    print("max y: %s" % max_y)

    print('')
    vent_map = VentMap(max_x, max_y)
    for vent in vents:
        vent_map.calc_line(vent[0], vent[1])

    vent_map.print_map()

    print("vent count: %s" % vent_map.vent_count)
    vent_map.calc_overlaps()
    return vents


if __name__ == "__main__":
    ap = argparse.ArgumentParser('day 05')
    ap.add_argument('input_file', help='file path to input')

    args = ap.parse_args()
    vents = parse_data(args.input_file)

    # vents = parse_data('/home/okim/dev/aoc2021/day05/test')
