# Part 1

with open('test', 'r') as f:
    lines = f.readlines()

inc_count = 0

for idx in range(1, len(lines)):    
    prev = int(lines[idx - 1])
    curr = int(lines[idx])
    if curr >= prev:
        inc_count += 1

print(inc_count)
