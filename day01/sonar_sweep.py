# Part 1

with open('input', 'r') as f:
    lines = f.readlines()
    data = [int(x) for x in lines]



inc_count = 0

for idx in range(1, len(data)):    
    prev = data[idx - 1]
    curr = data[idx]
    if curr >= prev:
        inc_count += 1

print(inc_count)

# Part 2
inc_count = 0
for idx in range(3, len(data)):
    a = data[idx - 3]
    b = data[idx - 2]
    c = data[idx - 1]
    d = data[idx]
    prev = a + b + c
    curr = b + c + d
    if curr > prev:
        inc_count += 1

print(inc_count)